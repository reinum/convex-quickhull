import random


def generate_random_coordinates(N, min_x, max_x, min_y, max_y):
    """
    Generates N random coordinates within the specified range.

    Args:
        N: Number of coordinates to generate.
        min_x: Minimum value for the X coordinate.
        max_x: Maximum value for the X coordinate.
        min_y: Minimum value for the Y coordinate.
        max_y: Maximum value for the Y coordinate.

    Returns:
        A list of N tuples, each representing an (X, Y) coordinate.
    """
    coordinates = []
    for _ in range(N):
        x = random.uniform(min_x, max_x)
        y = random.uniform(min_y, max_y)
        coordinates.append((x, y))
    return coordinates


# Example usage:
N = 10000  # Number of coordinates to generate
min_x = 0  # Minimum X value
max_x = 100  # Maximum X value
min_y = 0  # Minimum Y value
max_y = 100  # Maximum Y value

coordinates = generate_random_coordinates(N, min_x, max_x, min_y, max_y)


coors = ""
# Print the generated coordinates
for x, y in coordinates:
    coors += "{x:.2f} {y:.2f}\n"

open("points_10k.txt", "w").write(coors)
