def get_distance_to_next_vehicle(x_pos: int, road):
    """
    Calculates the distance to the next vehicle on the road.

    This function calculates the distance from the given position (`x_pos`) to the next 
    vehicle on the road, taking into account the vehicle's speed. It iterates over the 
    elements of the road array starting from the position ahead of the vehicle (`x_pos + 1`) 

    Parameters
    ----------
    x_pos : int
        The x-coordinate of the vehicle on the road.
    road : np.ndarray
        The state of the road.

    Returns
    -------
    int
        The distance to the next vehicle on the road.
    """
    if road[x_pos] == 0:
        raise ValueError('Cannot check distance from cell that does NOT contain vehicle.')

    distance = 0
    road_size = len(road)

    x_pos_to_check = x_pos + 1
    x_pos_to_check = 0 if x_pos_to_check == road_size else x_pos_to_check

    while (
        road[x_pos_to_check] == 0
        and x_pos_to_check != x_pos
    ):
        distance += 1
        x_pos_to_check = 0 if x_pos_to_check + 1 == road_size else x_pos_to_check + 1

    distance += 1

    return distance
