def get_distance_to_next_vehicle(x_pos: int, speed: int, road):
    """
    With provided road stat it calculate "almost" real distance.
    (!!) If the distance is greater than x_pos+speed+3 algorithm stop working
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
