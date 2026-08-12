# NeuroShell — LLM abstraction layer
import google.generativeai as genai
from google.generativeai.types import content_types
from app.core.config import Config

class LLMResponse:
    """Helper class to structure what the LLM returns."""
    def __init__(self, is_tool_call: bool, content: str = "", tool_name: str = "", tool_args: dict = None, raw_part=None):
        self.is_tool_call = is_tool_call
        self.content = content
        self.tool_name = tool_name
        self.tool_args = tool_args or {}
        self.raw_part = raw_part

class LLMClient:
    def __init__(self):
        genai.configure(api_key=Config.GEMINI_API_KEY)

    def generate(self, system_prompt: str, conversation_history: list[dict], available_tools: list[dict] = None) -> LLMResponse:
        
        # 1. Format tools for Gemini
        gemini_tools = [{"function_declarations": available_tools}] if available_tools else None

        model = genai.GenerativeModel(
            model_name=Config.GEMINI_MODEL,
            system_instruction=system_prompt,
            tools=gemini_tools
        )
        
        # 2. Convert our history into Gemini's exact format
        gemini_contents = []
        for msg in conversation_history:
            if msg["role"] == "user":
                gemini_contents.append({"role": "user", "parts": [msg["content"]]})
            elif msg["role"] == "assistant":
                gemini_contents.append({"role": "model", "parts": [msg["content"]]})
            elif msg["role"] == "tool_call":
                # When the LLM decided to use a tool in the past
                if "raw_part" in msg:
                    gemini_contents.append({"role": "model", "parts": [msg["raw_part"]]})
                else:
                    gemini_contents.append({
                        "role": "model", 
                        "parts": [{"function_call": {"name": msg["name"], "args": msg.get("args", {})}}]
                    })
            elif msg["role"] == "tool_result":
                # The result we gave back to the LLM
                # Note: some Gemini versions prefer role="function" here, but the python SDK usually maps this correctly.
                gemini_contents.append({
                    "role": "user", 
                    "parts": [{"function_response": {"name": msg["name"], "response": {"result": msg["content"]}}}]
                })

        # 3. Ask Gemini for the next step!
        try:
            response = model.generate_content(gemini_contents)
            part = response.candidates[0].content.parts[0]

            # 4. Check if Gemini decided to use a tool
            if part.function_call:
                return LLMResponse(
                    is_tool_call=True,
                    tool_name=part.function_call.name,
                    tool_args=dict(part.function_call.args),
                    raw_part=part
                )
            
            # Otherwise, it's just a normal text response
            return LLMResponse(
                is_tool_call=False,
                content=part.text
            )

        except Exception as e:
            raise RuntimeError(f"LLM error: {e}") from e
