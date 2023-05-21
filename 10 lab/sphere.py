import math

def calculate_volume(radius):
    return (4/3) * math.pi * radius ** 3

def calculate_surface_area(radius):
    return 4 * math.pi * radius ** 2

def calculate_mass(volume, density):
    return volume * density
