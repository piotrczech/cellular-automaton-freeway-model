import numpy as np


def generate_ones_array_with_expected_density(ones_density, size):
    desired_array = np.zeros(size)
    excepted_number_of_ones = int(np.floor(ones_density * size))

    rng = np.random.default_rng()
    desired_ones_positions = rng.choice(a=size, size=excepted_number_of_ones, replace=False)

    for position_to_place_one in desired_ones_positions:
        desired_array[position_to_place_one] = 1

    return desired_array


def should_accelerate_car(previous_road_state, x_position, car_velocity):
    first_cell_in_front_of = x_position + 1
    last_cell_in_front_of = first_cell_in_front_of + car_velocity + 1

    return np.sum(previous_road_state[first_cell_in_front_of:last_cell_in_front_of]) == 0


def simulate_with_history(L, v_max, density, p, steps):
    road = generate_ones_array_with_expected_density(ones_density=density, size=L)

    t_0 = L * 1

    history = np.zeros((steps + t_0, L)).astype(int)
    history[0] = road

    for i in range(1, steps + t_0):
        for j in range(L):
            cell = history[i - 1, j]

            if cell == 0:
                continue

            car_velocity = cell - 1 # becouse 0 is treated as Null
            new_x_position = j + car_velocity

            new_speed = car_velocity

            # 1) Acceleration
            if should_accelerate_car(
                previous_road_state=history[i - 1],
                x_position=new_x_position,
                car_velocity=car_velocity
            ):
                new_speed = min(v_max, car_velocity + 1)
            else:
                # find distance to next car
                new_speed = car_velocity
                for k in range(1, car_velocity + 1):
                    if new_x_position+k < L and history[i - 1, new_x_position + k] == 0:
                        new_speed = max(0, new_speed - 1)

            # 3) Randomization if greater than zero
            if np.random.random() <= p:
                new_speed = max(0, new_speed - 1)


            # 4) Each car is advanced
            # 4a) Car is outside of road, but this is circle move
            if (new_x_position > L - 1):
                new_x_position = new_x_position - L

            # 4b) Car is advanced speed sites
            correct_cell_value = new_speed + 1 # + 1, becouse 0 is Null in simulation
            history[i, new_x_position] = correct_cell_value

    # Return collection of data after the first t_0 time steps
    return history
    return history[t_0:]
