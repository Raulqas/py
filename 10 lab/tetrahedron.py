import math

def calculate_volume(base_area, height):
    return (1/3) * base_area * height

def calculate_surface_area(edge_length):
    return (math.sqrt(3) * edge_length ** 2) / 4

def calculate_mass(volume, density):
    return volume * density
