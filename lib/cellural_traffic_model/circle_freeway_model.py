import numpy as np

from lib.utils.generate_array_helper import generate_ones_array_with_expected_density
from lib.cellural_traffic_model import algorithm

def simulate_with_history(L: int, v_max: int, density: float, p: float, steps: int):
    """
        The model.
        -------

        (Based on article) Our computational model is defined on two-dimensional array
        of ("i" + "L" * 2) steps that each of them consist "L" sites array.

        Each site may either be occupied by one vehicle, or it may be empty.

        Each vehicle has an integer velocity with values between zero and v_max,
        but (!!) they are stored with additional + 1 value - and 0 is treated as empty site - no vehicle.

        One update of the system consists of the following four consecutive steps,
        which are performed in parallel for all vehicles:
        1. Accelerate
        2. Slowing down (due to other cars)
        3. Randomization
        4. Car motion
        
        Read more in article "A cellular automation model for freeway traffic"
        by Kai Nagel and Michael Schreckenberg

        Parameters
        ----------
        L : int
            Size of the road (number of cells).
        v_max : int
            Maximum speed for vehicle
        density : float, 0<=density<=1
            Density of vehicles in road, ranging from 0 to 1.
        p : float, 0<=density<=1
            Probability p, the velocity of each hivle is decreased by one, ranging from 0 to 1.
        steps : int
            Number of simulation steps to perform.

        Returns
        -------
        np.ndarray
            A two-dimensional array representing the simulation history, where each row corresponds 
            to a time step and each column corresponds to a cell on the road. The values represent 
            the velocities of vehicles at each cell and time step.
    """
    road = generate_ones_array_with_expected_density(ones_density=density, size=L)

    t_0 = L * 1

    history = np.zeros((steps + t_0, L)).astype(int)
    history[0] = road

    for i in range(1, steps + t_0):
        road_last_stage = history[i - 1]

        for vehicle_x in range(L):
            vehicle_value = road_last_stage[vehicle_x]

            if vehicle_value == 0:
                continue

            vehicle_velocity = vehicle_value - 1 # because 0 is treated as Null

            # 1. Accelerate
            vehicle_velocity = algorithm.accelerate_if_possible(vehicle_x, vehicle_velocity, road_last_stage, v_max)

            # 2. Slow down
            vehicle_velocity = algorithm.slow_down_if_needed(vehicle_x, vehicle_velocity, road_last_stage)

            # 3. Randomization if greater than zero
            vehicle_velocity = algorithm.slow_down_with_random(vehicle_velocity, p)

            # 4. Car motion
            algorithm.register_motion(history, i, L, vehicle_x, vehicle_velocity)

    # Return collection of data after the first t_0 time steps
    return history[t_0:]
