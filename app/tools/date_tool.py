
from app.actions.permissions import ActionPermission
from app.actions.base import BaseAction
from datetime import datetime

class GetDateAction(BaseAction):
    name = "get_date"
    description = "Returns the current system date"
    permission = ActionPermission.SAFE

    def get_schema(self) -> dict:
        return{
            "name":self.name,
            "description":self.description,
            "parameters":{
                "type":"object",
                "properties":{}
            }
        }
        
    def execute(self, **kwargs) -> str:
        current_date = datetime.now().strftime("%Y-%m-%d")
        return current_date