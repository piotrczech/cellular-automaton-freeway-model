import numpy as np

def main(L, v_max, density, p, steps):
    road = np.random.random(L) <= density
    road = road * np.ones(L)

    while np.sum(road) <= np.floor(density * L):
        road = np.random.random(L) <= density
        road = road * np.ones(L)

    N_cars = np.sum(road)

    t_0 = L * 1

    history = np.zeros((steps + t_0, L)).astype(int)
    history[0] = road

    for i in range(1, steps + t_0):
        # Generate new? - to powinno byc oparte na density
        # albo jezdza w koło?
        if N_cars <= np.floor(density * L):
            history[i, 0] = 4
            N_cars += 1

        for j in range(L):
            cell = history[i - 1, j]

            if cell == 0:
                continue

            car_velocity = cell - 1 # becouse 0 is treated as Null
            new_x_position = j + car_velocity

            new_speed = car_velocity

            # 1) Acceleration
            if np.sum(history[i - 1, (new_x_position+1):(new_x_position+1+car_velocity+1)]) == 0:
                new_speed = min(v_max, car_velocity + 1)
            else:
                # find distance to next car
                new_speed = car_velocity
                for k in range(1, car_velocity + 1):
                    if new_x_position+k < L and history[i - 1, new_x_position + k] == 0:
                        new_speed = max(0, new_speed - 1)

            # 3) Randomization
            if np.random.random() <= p:
                new_speed = max(0, new_speed - 1)


            # 4) Each car is advanced
            # 4a) Car is outside of road
            if (new_x_position >= L):
                N_cars -= 1
                continue

            # 4b) Car is advanced speed sites
            correct_cell_value = new_speed + 1 # + 1, becouse 0 is Null in simulation
            history[i, new_x_position] = correct_cell_value

    # Begin the collection of data after the first t_0 steps     
    # history = history[t_0:]
                   
    for line in history:
        line_as_strings = [str(x - 1) if x != 0 else "." for x in line]
        print(" ".join(line_as_strings))  # Połączenie łańcuchów spacją i wydrukowanie


main(
    L = 50,
    v_max = 5,
    density = 0.1,
    p = 0.4,
    steps = 1
)

