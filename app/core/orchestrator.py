from app.core.config import Config
from app.core.llm import LLMClient
import random
from app.core.context import ConversationContext
from app.prompts.system_prompt import SYSTEM_PROMPT
from app.core.router import IntentRouter

# Import our new Stage 2 systems
from app.actions.registry import ActionRegistry
from app.actions.executor import ActionExecutor
from app.tools.time_tool import GetTimeAction
from app.tools.date_tool import GetDateAction
from app.tools.calculator import CalculatorAction
from app.tools.system_info import SystemInfoAction

class Orchestrator:
    def __init__(self):
        Config.validate()
        self.llm = LLMClient()
        self.context = ConversationContext()
        self.router = IntentRouter()
        
        # 1. Setup the Action System!
        self.registry = ActionRegistry()
        self.registry.register(GetTimeAction())
        self.registry.register(GetDateAction())
        self.registry.register(CalculatorAction())
        self.registry.register(SystemInfoAction())
        
        self.executor = ActionExecutor(self.registry)
        
        # Create a list of schemas to send to the LLM
        self.schemas = [
            GetTimeAction().get_schema(),
            GetDateAction().get_schema(),
            CalculatorAction().get_schema(),
            SystemInfoAction().get_schema()
        ]

    def process(self, user_input: str) -> str:
        if not user_input or not user_input.strip():
            return "I didn't catch that. Could you say something?"

        self.context.add_message("user", user_input.strip())

        # 1. Ask the ML Router for the intent
        intent = self.router.route_request(user_input)
        print(f"\n[ROUTER] Intent identified: {intent}")

        # 2. Map deterministic intents directly to tools
        # Note: We only map tools we've actually built so far!
        intent_to_tool = {
            "GET_TIME": "get_time",
            "GET_DATE": "get_date",
            "SYSTEM_INFO": "get_system_info",
        }
        
        if intent in intent_to_tool:
            tool_name = intent_to_tool[intent]
            print(f"[ROUTER] ⚡ Bypassing Gemini! Directly executing '{tool_name}'...")
            
            # Execute the tool without asking Gemini
            tool_result = self.executor.execute_action(tool_name)
            
            # Create a simple deterministic response
            response = f"Result: {tool_result}"
            self.context.add_message("assistant", response)
            return response
            
        # 3. Handle GREETING deterministically without tools or Gemini
        if intent == "GREETING":
            print("[ROUTER] ⚡ Bypassing Gemini! Generating deterministic greeting...")
            greetings = [
                "Hi! How can I help you?",
                "Hello! What can I do for you?",
                "Hey! I'm listening.",
                "Hi there! What's up?"
            ]
            response = random.choice(greetings)
            self.context.add_message("assistant", response)
            return response
            
        # 4. For GENERAL_QUESTION, UNKNOWN, or intents needing args (like Calculator), fallback to Gemini!
        print("[ROUTER] 🧠 Falling back to Gemini LLM...")

        # 5. We need a loop! Because the LLM might ask for a tool, get the result, 
        # and then ask for ANOTHER tool before giving a final answer.
        MAX_TURNS = 5
        
        for _ in range(MAX_TURNS):
            try:
                # 3. Call generate, passing in the system_prompt, history, AND self.schemas!
                response = self.llm.generate(
                    system_prompt=SYSTEM_PROMPT,
                    conversation_history=self.context.get_history(),
                    available_tools=self.schemas
                )
                if response.is_tool_call:
                    # 4. Save the LLM's request to context so it remembers it asked!
                    self.context.add_message("tool_call", f"Tool: {response.tool_name}", name=response.tool_name, args=response.tool_args, raw_part=response.raw_part)
                    
                    print(f"\n[ACTION ENGINE] Executing '{response.tool_name}'...")
                    
                    # 5. Execute the tool!
                    tool_result = self.executor.execute_action(response.tool_name, **response.tool_args)
                    
                    # 6. Save the result back to context so the LLM can read it!
                    self.context.add_message("tool_result", str(tool_result), name=response.tool_name)
                    
                    # The loop restarts, sending this new context back to Gemini!
                    continue
                else:
                    # It's a text response! Save it and return it.
                    self.context.add_message("assistant", response.content)
                    return response.content

            except Exception as e:
                error_str = str(e)
                if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                    fallback = "I'm sorry, my API quota is currently exhausted. Please try again later."
                    self.context.add_message("assistant", fallback)
                    return fallback
                elif "503" in error_str or "UNAVAILABLE" in error_str:
                    fallback = "I'm sorry, the Google servers are currently experiencing high demand. Please try again later."
                    self.context.add_message("assistant", fallback)
                    return fallback
                else:
                    return f"⚠️ Something went wrong: {error_str}"
                
        return "⚠️ Error: The AI got stuck in a loop and tried to use too many tools."
