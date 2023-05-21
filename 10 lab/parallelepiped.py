def calculate_volume(length, width, height):
    return length * width * height

def calculate_surface_area(length, width, height):
    return 2 * (length * width + width * height + length * height)

def calculate_mass(volume, density):
    return volume * density
