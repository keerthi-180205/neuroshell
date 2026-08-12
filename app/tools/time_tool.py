from app.actions.permissions import ActionPermission
from app.actions.base import BaseAction
from datetime import datetime

class GetTimeAction(BaseAction):
    
    # 1. Give it a name and description
    name = "get_time"
    description = "Returns the current system time."
    permission = ActionPermission.SAFE

    # 2. Implement the schema method
    def get_schema(self) -> dict:
        # Gemini needs to know what arguments this tool takes.
        # Since getting the time requires no arguments, the properties are empty!
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": {} # No arguments needed
            }
        }

    # 3. Implement the execute method
    def execute(self, **kwargs) -> str:
        # Get the current time using Python's datetime library
        # Format it as HH:MM:SS
        current_time = datetime.now().strftime("%H:%M:%S")
        
        # Return the string so the Executor can send it to Gemini!
        return current_time
