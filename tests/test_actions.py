import pytest
from app.actions.registry import ActionRegistry
from app.actions.executor import ActionExecutor
from app.tools.calculator import CalculatorAction

def test_registry_can_register_and_get():
    # 1. Create a new ActionRegistry
    registry = ActionRegistry()
    
    # 2. Create a new CalculatorAction
    calc_tool = CalculatorAction()
    
    # 3. Register the tool
    registry.register(calc_tool)
    
    # 4. Get the tool back out
    retrieved_tool = registry.get("calculator")
    
    # 5. Assert (check) that the retrieved tool is the same one we put in!
    assert retrieved_tool.name == "calculator"

def test_executor_runs_calculator():
    registry = ActionRegistry()
    registry.register(CalculatorAction())
    executor = ActionExecutor(registry)
    
    # Use the executor to run the calculator with expression "5 * 5"
    result = executor.execute_action("calculator", expression="5 * 5")
    
    # Assert that the result is what we expect!
    assert result == "25"

def test_executor_handles_missing_tool():
    registry = ActionRegistry()
    executor = ActionExecutor(registry) # Empty registry!
    
    # Try to execute a tool that doesn't exist
    result = executor.execute_action("fake_tool")
    
    # Assert that the result contains the word "Error"
    assert "Error" in result
