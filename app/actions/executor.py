"""Action executor for validating and running tools."""

# We will implement the ActionExecutor class here.

from app.actions.registry import ActionRegistry
from typing import Any

class ActionExecutor:
    def __init__(self, registry: ActionRegistry):
        # The executor needs access to the registry to find tools
        self.registry = registry

    def execute_action(self, action_name: str, **kwargs) -> Any:
        """Find the action in the registry and execute it.
        
        Args:
            action_name: The name of the tool (e.g., 'calculator')
            **kwargs: The arguments to pass to the tool
            
        Returns:
            The result of the tool, or an error string if something went wrong.
        """
        try:
            # 1. Get the action from self.registry
            action = self.registry.get(action_name)

            # 2. Call the execute method on the action with **kwargs
            result = action.execute(**kwargs)

            # 3. Return the result
            return result

        except KeyError:
            # If the tool isn't in the registry, return an error string
            return f"Error: Tool '{action_name}' not found."
        except Exception as e:
            # If the tool crashes while running, return the error
            return f"Error executing '{action_name}': {str(e)}"
