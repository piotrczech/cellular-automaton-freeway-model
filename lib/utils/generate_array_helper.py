import numpy as np

def generate_ones_array_with_expected_density(ones_density: int, size: int):
    """
    Generate new ndarray with given density that will pick random spots for "ones"
    """
    desired_array = np.zeros(size)
    excepted_number_of_ones = int(np.floor(ones_density * size))

    rng = np.random.default_rng()
    desired_ones_positions = rng.choice(a=size, size=excepted_number_of_ones, replace=False)

    for position_to_place_one in desired_ones_positions:
        desired_array[position_to_place_one] = 1

    return desired_array