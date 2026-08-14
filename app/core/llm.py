# NeuroShell — LLM abstraction layer
from google import genai
from google.genai import types
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
        self.client = genai.Client(api_key=Config.GEMINI_API_KEY)

    def generate(self, system_prompt: str, conversation_history: list[dict], available_tools: list[dict] = None) -> LLMResponse:
        
        # 1. Format tools for Gemini
        gemini_tools = [{"function_declarations": available_tools}] if available_tools else None
        
        config_kwargs = {}
        if system_prompt:
             config_kwargs["system_instruction"] = system_prompt
        if gemini_tools:
             config_kwargs["tools"] = gemini_tools
             
        config = types.GenerateContentConfig(**config_kwargs)

        # 2. Convert our history into Gemini's exact format
        gemini_contents = []
        for msg in conversation_history:
            if msg["role"] == "user":
                gemini_contents.append({"role": "user", "parts": [{"text": msg["content"]}]})
            elif msg["role"] == "assistant":
                gemini_contents.append({"role": "model", "parts": [{"text": msg["content"]}]})
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
                gemini_contents.append({
                    "role": "user", 
                    "parts": [{"function_response": {"name": msg["name"], "response": {"result": msg["content"]}}}]
                })

        # 3. Ask Gemini for the next step!
        try:
            response = self.client.models.generate_content(
                model=Config.GEMINI_MODEL,
                contents=gemini_contents,
                config=config
            )
            part = response.candidates[0].content.parts[0]

            # 4. Check if Gemini decided to use a tool
            if part.function_call:
                return LLMResponse(
                    is_tool_call=True,
                    tool_name=part.function_call.name,
                    tool_args=part.function_call.args if part.function_call.args else {},
                    raw_part=part
                )
            
            # Otherwise, it's just a normal text response
            return LLMResponse(
                is_tool_call=False,
                content=part.text
            )

        except Exception as e:
            raise RuntimeError(f"LLM error: {e}") from e
