from enum import Enum

class ActionPermission(Enum):
    """Defines the permission levels required to execute a tool.
    
    SAFE: Can be executed automatically without user intervention (e.g., math, time).
    READ_ONLY: Reads system data but does not mutate state. Can run automatically.
    CONFIRMATION_REQUIRED: Dangerous actions (e.g., delete file). Must ask the human first.
    """
    SAFE = "safe"
    READ_ONLY = "read_only"
    CONFIRMATION_REQUIRED = "confirmation_required"
