import numpy as np

def main(L, v_max, p_start, p_game, steps):
    road = np.random.random(L) <= p_start
    road = road * np.random.randint(1, v_max, L)

    history = np.zeros((steps, L)).astype(int)
    history[0] = road

    for i in range(1, steps):
        # Generate new? - nie wiem czy to powinno byc
        if np.random.random() <= p_start:
            history[i, 0] = np.random.randint(1, v_max)

        for j in range(L):
            speed = history[i - 1, j]

            if speed == 0:
                continue

            # 1) Acceleration
            if np.sum(history[i - 1, (j+1):(j+speed+1)]) == 0:
                new_speed = min(v_max, speed + 1)
            # 2) Slowing down:
            else:
                new_speed = max(1, speed - 1)

            # 3) Randomization
            if np.random.random() <= p_game:
                new_speed = max(1, speed - 1)


            # 4) Each car is advanced
            # 4a) Car is outside of road
            if (j + speed >= L):
                break

            # 4b) Car is advanced speed sites
            history[i, j + speed] = new_speed

                   
    for line in history:
        line_as_strings = [str(x) if x != 0 else "." for x in line]
        print(" ".join(line_as_strings))  # Połączenie łańcuchów spacją i wydrukowanie

main(
    L = 50,
    v_max = 5,
    p_start = 0.05,
    p_game = 0.2,
    steps = 15
)

