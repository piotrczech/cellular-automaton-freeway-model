import road_helper
import numpy as np

def test_correct_distance_in_front():
    """
    Test the calculation of the correct distance to the next vehicle in front.
    """
    road = np.array([1, 0, 0, 1, 0])
    distance = road_helper.get_distance_to_next_vehicle(x_pos = 0, road = road)

    assert distance == 3

def test_correct_distance_in_circle_closed_road():
    """
    Test the calculation of distance when vehicles are adjacent.
    """
    road = np.array([1, 0, 0, 1, 0])
    distance = road_helper.get_distance_to_next_vehicle(x_pos = 3, road = road)

    assert distance == 2

    road = np.array([0, 0, 1, 0, 1])
    distance = road_helper.get_distance_to_next_vehicle(x_pos = 4, road = road)

    assert distance == 3

def test_distance_if_vehicles_are_adjacent():
    """
    Test the calculation of distance when vehicles are adjacent.
    """
    road = np.array([1, 1])
    distance = road_helper.get_distance_to_next_vehicle(x_pos = 0, road = road)

    assert distance == 1