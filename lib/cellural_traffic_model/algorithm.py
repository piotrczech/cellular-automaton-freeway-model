import numpy as np

from lib.utils.road_helper import get_distance_to_next_vehicle

def accelerate_if_possible(vehicle_x: int, vehicle_velocity: int, road_last_stage, v_max: int):
    """
    Acceleration.
    -------
    If the vehicle_velocity (v) is lower than v_max and if the distance to the next car ahed
    is larger than v + 1, the speed is advanced by one [v -> v + 1]

    Parameters
    ----------
    vehicle_x : int
        The x-coordinate of the vehicle on the road.
    vehicle_velocity : int
        The current velocity of the vehicle.
    road_last_stage : np.ndarray
        The state of the road at the last stage.
    v_max : int
        The maximum velocity allowed.

    Returns
    -------
    int
        The new velocity of the vehicle after acceleration.
    """
    distance_to_next_vehicle = get_distance_to_next_vehicle(vehicle_x, road_last_stage)

    if (
        distance_to_next_vehicle > vehicle_velocity + 1
        and vehicle_velocity < v_max
    ):
        return vehicle_velocity + 1

    return vehicle_velocity


def slow_down_if_needed(vehicle_x: int, vehicle_velocity: int, road_last_stage):
    """
    Slowing down.
    -------
    (due to other cars): If a vehicle at site i sees the next vehicle at site i + j (with j <= v),
    it reduces its speed to j - 1 [v -> j - 1]

    Parameters
    ----------
    vehicle_x : int
        The x-coordinate of the vehicle on the road.
    vehicle_velocity : int
        The current velocity of the vehicle.
    road_last_stage : np.ndarray
        The state of the road at the last stage.

    Returns
    -------
    int
        The new velocity of the vehicle after deceleration.
    """
    distance_to_next_vehicle = get_distance_to_next_vehicle(vehicle_x, road_last_stage)

    if (distance_to_next_vehicle <= vehicle_velocity):
        return distance_to_next_vehicle - 1
    
    return vehicle_velocity


def slow_down_with_random(vehicle_velocity: int, p: float):
    """
    Randomization.
    -------
    With probability p the velocity of vehicle (if greater than zero) is decreased by one [v -> v -1]

    Parameters
    ----------
    vehicle_velocity : int
        The current velocity of the vehicle.
    p : float
        The probability of randomization.

    Returns
    -------
    int
        The new velocity of the vehicle after randomization.
    """
    if np.random.random() <= p and vehicle_velocity > 0:
        return vehicle_velocity - 1
    
    return vehicle_velocity


def register_motion(history, history_current_step: int, road_size: int, vehicle_x: int, vehicle_velocity: int):
    """
    Car motion.
    -------
    Each vehicle is advanced v sites.

    Parameters
    ----------
    history : np.ndarray
        The history of the road simulation.
    history_current_step : int
        The current time step.
    road_size : int
        The size of the road.
    vehicle_x : int
        The x-coordinate of the vehicle on the road.
    vehicle_velocity : int
        The velocity of the vehicle.
    """
    vehicle_velocity = max(0, vehicle_velocity)

    vehicle_new_x = (vehicle_x + vehicle_velocity) % road_size
    vehicle_new_value = vehicle_velocity + 1

    # ?? - w połowie jeszcze rozumiem czemu tak działa
    history[history_current_step - 1, vehicle_x] = vehicle_new_value
    history[history_current_step, vehicle_new_x] = vehicle_new_value
