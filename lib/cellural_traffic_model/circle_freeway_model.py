import numpy as np

from lib.utils.generate_array_helper import generate_ones_array_with_expected_density
from lib.cellural_traffic_model import algorithm

def simulate_with_history(L, v_max, density, p, steps):
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

            vehicle_velocity = vehicle_value - 1 # becouse 0 is treated as Null

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
