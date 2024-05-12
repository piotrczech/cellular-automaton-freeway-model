from lib.utils.display.strategies import DisplayStrategy

class DisplaySimulationContext:
    """
    DisplaySimulationContext 
    ----------
    The Context class defines the interface for display strategies.

    Implemented using the Strategy design pattern.
    @doc https://refactoring.guru/design-patterns/strategy/python/example

    Parameters
    ----------
    display_strategy (object): An object representing the display strategy.
        It must implement the display(road_history) method, which is called
        by the context to display simulation data.

    Attributes
    -------
    display_strategy (object): An object representing the display strategy.

    Raises
    -------
    TypeError: If display_strategy is not an object.

    """
    
    def __init__(self, display_strategy: DisplayStrategy) -> None:
        """
        Constructor for the DisplaySimulationContext class.

        Parameters
        ----------
            display_strategy (object): An object representing the display strategy.
                It must implement the display(road_history) method, which is called
                by the context to display simulation data.

        Raises
        -------
        TypeError: If display_strategy is not an object.

        Returns
        -------
        None

        """

        if not isinstance(display_strategy, object):
            raise TypeError("display_strategy must be an object.")

        self.display_strategy = display_strategy

    def display(self, road_history):
        """
        Displays simulation data in the specified format.

        Parameters
        ----------
        road_history (list): A list containing the history of road simulation.

        Returns
        -------
        None

        """
        return self.display_strategy.display(road_history)