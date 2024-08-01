from math import sqrt

def hexagon_coordinates_to_screen_coordinates(radius, hexagon_x, hexagon_z):
    x_coordinate = sqrt(3) * radius * (hexagon_x + hexagon_z / 2)
    y_coordinate = 3 / 2 * radius * hexagon_z
    return (x_coordinate, y_coordinate)


# Not 100% sure if this function works properly