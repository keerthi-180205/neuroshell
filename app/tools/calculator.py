# NeuroShell — Calculator tool (math operations)
from app.actions.permissions import ActionPermission
from app.actions.base import BaseAction

class CalculatorAction(BaseAction):
    
    # 1. Name and description
    name = "calculator"
    description = "Evaluates a mathematical expression and returns the result."
    permission = ActionPermission.SAFE

    # 2. The Schema
    def get_schema(self) -> dict:
        # Notice how this time we are NOT returning empty properties.
        # We are telling Gemini that it MUST provide an "expression" string.
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "The math expression to evaluate, like '25 * 48' or '100 / 4'"
                    }
                },
                "required": ["expression"]
            }
        }

    # 3. Execution Logic
    def execute(self, **kwargs) -> str:
        # Step A: Get the expression from kwargs.
        expression = kwargs.get("expression")
        
        # Remember, Gemini passes it in as a dictionary! 
        # Example: kwargs will look like {"expression": "25 * 48"}
        
        # Step B: Check if the expression exists. If not, return an error string.
        if not expression:
            return "Error: No expression provided"
        # Step C: Use a try/except block.

        try:
            result = eval(expression)
            return str(result)
        except Exception as e:
            return f"Error: {str(e)}"
