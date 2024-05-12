from abc import ABC, abstractmethod
import matplotlib.pyplot as plt

class DisplayStrategy(ABC):
    """
    The Strategy interface defines a method for displaying simulation data.

    The DisplaySimulationContext uses this interface to call the display method
    """

    @abstractmethod
    def display(self, road_history):
        """
        Display method to be implemented by concrete strategies.
        """
        pass


class ConsoleDisplayStrategy(DisplayStrategy):
    """
    Concrete strategy: displays simulation data in the console.
    """

    def display(road_history):
        """
        Display monte carlo simulation data as a scatter plot.
        """
        for line in road_history:
            line_as_strings = [str(x - 1) if x != 0 else "." for x in line]
            print(" ".join(line_as_strings))  # Połączenie łańcuchów spacją i wydrukowanie
        

class ScatterPlotDisplayStrategy(DisplayStrategy):
    """
    Concrete strategy: displays simulation data as a scatter plot.
    """
    def display(road_history):
        """
        Display monte carlo simulation data as a scatter plot.
        """
        steps = len(road_history)
        x = []
        y = []

        for history_index, road_history_line in enumerate(road_history):
            for x_pos, cell_value in enumerate(road_history_line):

                if cell_value == 0:
                    continue

                x.append(x_pos)
                y.append(steps - history_index)
        
        plt.xlabel = "Space (road)"
        plt.ylabel = "Time (going down)"

        plt.scatter(x, y, c='black', alpha=0.15, s=2)
        plt.show()


class LinePlotDisplayStrategy:
    """
    The Strategy interface that present output as line matplotlib plot

    The DisplaySimulationContext uses this interface to call the display method
    """
    def display(road_history):
        """
        Display monte carlo simulation data as scatter aerial plot
        """

        steps = len(road_history)

        for history_index, road_history_line in enumerate(road_history):

            for x_pos, cell_value in enumerate(road_history_line):

                if cell_value == 0:
                    continue

                vehicle_speed = cell_value - 1
            
                x_start = x_pos
                y_start = steps - history_index

                x_end = x_pos + vehicle_speed
                y_end = steps - history_index - 1

                alpha = min(1, 1 / max(vehicle_speed, 0.1))
                
                plt.plot([x_start, x_end], [y_start, y_end], c='black', alpha=alpha)
        
        plt.show()
