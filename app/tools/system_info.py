# NeuroShell — System info tool (CPU, RAM, disk — read-only)

from app.actions.permissions import ActionPermission
from app.actions.base import BaseAction
import platform

class SystemInfoAction(BaseAction):
    name = "get_system_info"
    description = "Returns the system information, including OS, CPU, RAM, and disk usage."
    permission = ActionPermission.READ_ONLY

    def get_schema(self)->dict:
        return{
            "name" : self.name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }

    def execute(self, **kwargs) -> str:
        info = {
            "os": platform.platform(),
            "python_version": platform.python_version(),
            "architecture": platform.architecture(),
            "machine": platform.machine(),
        }
        return str(info)