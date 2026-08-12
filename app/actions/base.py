"""Base classes for NeuroShell Actions."""

# We will define the BaseAction and ToolRequest/ToolResult models here.

from app.actions.permissions import ActionPermission
from abc import ABC, abstractmethod
from typing import Any

class BaseAction(ABC):
    """Base blueprint for all NeuroShell actions.
    
    Every tool must inherit from this class and implement
    the required properties and methods.
    """
    
    # 1. Every action needs a name and a description
    name: str
    description: str
    permission : ActionPermission

    # 2. Every action must provide a schema for the LLM
    @abstractmethod
    def get_schema(self) -> dict:
        """Return the JSON schema that describes this tool to Gemini."""
        pass

    # 3. Every action must have execution logic
    @abstractmethod
    def execute(self, **kwargs) -> Any:
        """Run the actual tool logic and return the result.
        
        Args:
            **kwargs: The arguments provided by the LLM.
            
        Returns:
            Any: The result of the action (string, dict, etc.)
        """
        pass
