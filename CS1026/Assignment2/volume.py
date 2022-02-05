import math


def volume_of_cube(side_length):
    volume = side_length ** 3
    return volume


def volume_of_pyramid(base_length, height):
    volume = (base_length**2)*height/3
    return volume


def volume_of_ellipsoid(first_radius, second_radius, third_radius):
    volume = (first_radius*second_radius*third_radius)*4/3*math.pi
    return volume