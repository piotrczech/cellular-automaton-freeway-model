class DisplaySimulationContext:
    """
    The Context defines the interface of interest to display strategies.

    Implemented with strategy design pattern.
    @doc https://refactoring.guru/design-patterns/strategy/python/example
    """
    
    def __init__(self, display_strategy) -> None:
        """
        The Context accepts a display strategy through the constructor
        """
        self.display_strategy = display_strategy
        pass

    def display(self, road_history):
        """
        Method to display in expected format monte carlo road history data,
        that are stored as two-dimensional arrays
        """
        return self.display_strategy.display(road_history)