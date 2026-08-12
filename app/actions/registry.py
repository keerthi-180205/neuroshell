"""Action registry for managing available tools."""

# We will implement the ActionRegistry class here.


from app.actions.base import BaseAction

class ActionRegistry:
    def __init__(self):
        # We need a dictionary to store our actions
        self._actions: dict[str, BaseAction] = {}
        
    def register(self, action: BaseAction) -> None:

        """Add a new action to the registry.
        
        Args:
            action: The tool/action to register.
            
        Raises:
            ValueError: If an action with that name already exists.
        """

        if action.name in self._actions:
            raise ValueError(f"Action '{action.name}' is already registered.")
        self._actions[action.name] = action
        
    def get(self, name: str) -> BaseAction:

        """Retrieve an action by its name.
        
        Args:
            name: The exact name of the tool (e.g., 'get_time').
            
        Returns:
            The BaseAction instance.
            
        Raises:
            KeyError: If the tool is not found in the registry.
        """

        action = self._actions.get(name)
        if not action:
            raise KeyError(f"Unknown action {name}")
        return action
        
    def list_actions(self) -> list[str]:
        """Return a list of all available tool names."""
        return list(self._actions.keys())

