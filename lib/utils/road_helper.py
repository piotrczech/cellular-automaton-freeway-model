def get_distance_to_next_vehicle(x_pos: int, speed: int, road):
    """
    Calculates the distance to the next vehicle on the road.

    This function calculates the distance from the given position (`x_pos`) to the next 
    vehicle on the road, taking into account the vehicle's speed. It iterates over the 
    elements of the road array starting from the position ahead of the vehicle (`x_pos + 1`) 
    up to `x_pos + speed + 2` to determine the distance. If the distance is greater than 
    `x_pos + speed + 3`, the calculation stops, as it is considered unnecessary.

    Parameters
    ----------
    x_pos : int
        The x-coordinate of the vehicle on the road.
    speed : int
        The current velocity of the vehicle.
    road : np.ndarray
        The state of the road.

    Returns
    -------
    int
        The distance to the next vehicle on the road.
    """
    x_pos_start = x_pos + 1
    x_pos_end = x_pos_start + speed + 2 # +2 - is safe number that wystarcza to calcute distance. Higher distance is useless.
    view_in_front_of_vehicle = road[x_pos_start : x_pos_end]

    distance = 0

    for vehicle_value in view_in_front_of_vehicle:
        if vehicle_value != 0:
            break

        distance += 1

    # If the world end with the distance:
    if x_pos + distance + 1 >= len(road):
        return 10

    return distance
