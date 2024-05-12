import numpy as np

from lib.utils.road_helper import get_distance_to_next_vehicle

def accelerate_if_possible(vehicle_x: int, vehicle_velocity: int, road_last_stage, v_max: int):
    """
    Acceleration.
    -------

    if the vehicle_velocity (v) is lower than v_max and if the distance to the next car ahed
    is larger than v + 1, the speed is advanced by one [v -> v + 1]
    """
    distance_to_next_vehicle = get_distance_to_next_vehicle(vehicle_x, vehicle_velocity, road_last_stage)

    if (
        distance_to_next_vehicle > vehicle_velocity + 1
        and vehicle_velocity < v_max
    ):
        return vehicle_velocity + 1

    return vehicle_velocity


def slow_down_if_needed(vehicle_x, vehicle_velocity, road_last_stage):
    """
    Slowing down.
    -------

    (due to other cars): if a vehicle at site i sees the next vehicle at site i + j (with j <= v),
    it reduces its speed to j - 1 [v -> j - 1]
    """
    distance_to_next_vehicle = get_distance_to_next_vehicle(vehicle_x, vehicle_velocity, road_last_stage)

    if (distance_to_next_vehicle <= vehicle_velocity):
        return distance_to_next_vehicle
    
    return vehicle_velocity


def slow_down_with_random(vehicle_velocity, p):
    """
    Randomization.
    -------

    with probability p the velocity of vehicle (if greater than zero) is decreased by one [v -> v -1]
    """
    if np.random.random() <= p and vehicle_velocity > 0:
        return vehicle_velocity - 1
    
    return vehicle_velocity


def register_motion(history, history_current_step, road_size, vehicle_x, vehicle_velocity):
    """
    Car motion.
    -------

    each vehicle is advanced v sites.
    """
    vehicle_velocity = max(0, vehicle_velocity)

    vehicle_new_x = (vehicle_x + vehicle_velocity) % road_size
    vehicle_new_value = vehicle_velocity + 1

    # ?? - w połowie jeszcze rozumiem czemu tak działa
    history[history_current_step - 1, vehicle_x] = vehicle_new_value
    history[history_current_step, vehicle_new_x] = vehicle_new_value
