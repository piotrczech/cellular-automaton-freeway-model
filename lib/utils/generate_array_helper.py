import numpy as np

def generate_ones_array_with_expected_density(ones_density: int, size: int):
    """
    Generates a new ndarray with the specified density of ones.

    This function creates a new numpy array of the given size, where approximately 
    `ones_density * size` elements are set to 1, chosen randomly.

    Parameters
    ----------
    ones_density : float
        The desired density of ones in the array, ranging from 0 to 1.
    size : int
        The size of the array to be generated.

    Returns
    -------
    np.ndarray
        A numpy array of size `size` with approximately `ones_density * size` elements set to 1.
    """
    desired_array = np.zeros(size)
    excepted_number_of_ones = int(np.floor(ones_density * size))

    rng = np.random.default_rng()
    desired_ones_positions = rng.choice(a=size, size=excepted_number_of_ones, replace=False)

    for position_to_place_one in desired_ones_positions:
        desired_array[position_to_place_one] = 1

    return desired_array