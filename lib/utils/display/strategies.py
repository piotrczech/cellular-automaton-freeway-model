class ConsoleDisplayStrategy:
    """
    The Strategy interface that present output in console

    The DisplaySimulationContext uses this interface to call the display method
    """

    def display(road_history):
        """
        Display monte carlo simulation data in console
        """
        for line in road_history:
            line_as_strings = [str(x - 1) if x != 0 else "." for x in line]
            print(" ".join(line_as_strings))  # Połączenie łańcuchów spacją i wydrukowanie