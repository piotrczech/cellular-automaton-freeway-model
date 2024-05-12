import generate_array_helper
import numpy as np

def test_correct_number_of_ones_with_boundary_density():
    """
    Test the generation of an array with the correct number of ones for boundary density.
    """
    ones_array = generate_array_helper.generate_ones_array_with_expected_density(1, 3) 

    assert list(ones_array) == [1, 1, 1]

    zeros_array = generate_array_helper.generate_ones_array_with_expected_density(0, 3) 

    assert list(zeros_array) == [0, 0, 0]

def test_if_generated_array_type_is_numpy_array():
    """
    Test the returned array type.
    """
    some_array = generate_array_helper.generate_ones_array_with_expected_density(1, 1) 

    assert isinstance(some_array, np.ndarray)

def test_generate_array_with_different_densities():
    """
    Test the returned array type.
    """

    for expected_number_of_ones in range(1, 9):
        density = expected_number_of_ones / 10
        tested_array = generate_array_helper.generate_ones_array_with_expected_density(density, 10) 
        assert np.sum(tested_array) == expected_number_of_ones
