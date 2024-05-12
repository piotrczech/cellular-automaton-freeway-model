import pytest
from core import DisplaySimulationContext, DisplayStrategy


class DummyDisplayStrategy(DisplayStrategy):
    def display(self, road_history):
        return "Dummy display"


def test_display_simulation_context_construction():
    """
    Test the construction of DisplaySimulationContext.
    """

    display_strategy = DummyDisplayStrategy()
    context = DisplaySimulationContext(display_strategy)

    assert isinstance(context, DisplaySimulationContext)


def test_display_simulation_context_construction_invalid_strategy():
    """
    Test the construction of DisplaySimulationContext with an invalid display strategy.
    """
    with pytest.raises(TypeError, match="display_strategy must be an object with display method."):
        DisplaySimulationContext("invalid_strategy")


def test_display_simulation_context_display():
    """
    Test the display method of DisplaySimulationContext.
    """
    display_strategy = DummyDisplayStrategy()
    context = DisplaySimulationContext(display_strategy)

    assert context.display([]) == "Dummy display"
