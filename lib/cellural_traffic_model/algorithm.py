import numpy as np

from lib.utils.road_helper import get_distance_to_next_vehicle

def accelerate_if_possible(vehicle_x, vehicle_velocity, road_last_stage, v_max):
    distance_to_next_vehicle = get_distance_to_next_vehicle(vehicle_x, vehicle_velocity, road_last_stage)

    if (
        distance_to_next_vehicle > vehicle_velocity + 1
        and vehicle_velocity < v_max
    ):
        return vehicle_velocity + 1

    return vehicle_velocity


def slow_down_if_needed(vehicle_x, vehicle_velocity, road_last_stage):
    distance_to_next_vehicle = get_distance_to_next_vehicle(vehicle_x, vehicle_velocity, road_last_stage)

    if (distance_to_next_vehicle <= vehicle_velocity):
        return distance_to_next_vehicle
    
    return vehicle_velocity


def slow_down_with_random(vehicle_velocity, p):
    if np.random.random() <= p:
        return vehicle_velocity - 1
    
    return vehicle_velocity


def register_motion(history, history_current_step, road_size, vehicle_x, vehicle_velocity):
    vehicle_velocity = max(0, vehicle_velocity)

    vehicle_new_x = (vehicle_x + vehicle_velocity) % road_size
    vehicle_new_value = vehicle_velocity + 1

    # ?? - w połowie jeszcze rozumiem czemu tak działa
    history[history_current_step - 1, vehicle_x] = vehicle_new_value
    history[history_current_step, vehicle_new_x] = vehicle_new_value
    
