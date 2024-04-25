#!/usr/bin/env python3.11

from lib.cellural_traffic_model import circle_freeway_model

def main():
    road_history = circle_freeway_model.simulate_with_history(
        L = 50,
        v_max = 5,
        density = 0.1,
        p = 0.3,
        steps = 10
    )

    for line in road_history:
        line_as_strings = [str(x - 1) if x != 0 else "." for x in line]
        print(" ".join(line_as_strings))  # Połączenie łańcuchów spacją i wydrukowanie

if __name__ == "__main__":
    main()
