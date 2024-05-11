import numpy as np

def get_distance_to_next_vehicle(x_pos, speed, road):
    view_in_front_of_vehicle = road[(x_pos + 1) : (x_pos + speed + 3)] # 3 - is safe number that wystarcza to calcute distance. Higher distance is useless.

    distance = 0

    for vehicle_value in view_in_front_of_vehicle:
        if vehicle_value != 0:
            break

        distance += 1

    # If the world end with the distance:
    if x_pos + distance + 1 >= len(road):
        return 10

    return distance

def generate_ones_array_with_expected_density(ones_density, size):
    desired_array = np.zeros(size)
    excepted_number_of_ones = int(np.floor(ones_density * size))

    rng = np.random.default_rng()
    desired_ones_positions = rng.choice(a=size, size=excepted_number_of_ones, replace=False)

    for position_to_place_one in desired_ones_positions:
        desired_array[position_to_place_one] = 1

    return desired_array

def simulate_with_history(L, v_max, density, p, steps):
    road = generate_ones_array_with_expected_density(ones_density=density, size=L)

    t_0 = L * 1

    road = np.zeros(L)
    road[8] = 5
    road[25] = 6
    road[32] = 6
    road[40] = 6
    road[49] = 1
    road[50] = 1
    road[52] = 2
    road[60] = 5

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
            distance_to_next_vehicle = get_distance_to_next_vehicle(vehicle_x, vehicle_velocity, road_last_stage)
            if (
                distance_to_next_vehicle > vehicle_velocity + 1
                and vehicle_velocity < v_max
            ):
                vehicle_velocity += 1

            # 2. Slow down
            distance_to_next_vehicle = get_distance_to_next_vehicle(vehicle_x, vehicle_velocity, road_last_stage)
            if (distance_to_next_vehicle <= vehicle_velocity):
                vehicle_velocity = distance_to_next_vehicle

            # 3) Randomization if greater than zero
            if np.random.random() <= p:
                vehicle_velocity -= 1

            vehicle_velocity = max(0, vehicle_velocity)

            vehicle_new_x = (vehicle_x + vehicle_velocity) % L
            vehicle_new_value = vehicle_velocity + 1

            # ?? - w połowie jeszcze rozumiem czemu tak działa
            history[i - 1, vehicle_x] = vehicle_new_value
            history[i, vehicle_new_x] = vehicle_new_value

    # Return collection of data after the first t_0 time steps
    return history[t_0:]
