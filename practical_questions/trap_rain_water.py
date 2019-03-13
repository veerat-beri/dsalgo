# Problem Statement
# https://www.geeksforgeeks.org/trapping-rain-water/


def get_trapped_water_volume(elevation_map):
    total_walls = len(elevation_map)
    max_left_elevation = [0]*total_walls
    max_right_elevation = [0]*total_walls

    max_left_elevation_so_far = max_left_elevation[0] = elevation_map[0]

    for wall_index in range(1, total_walls):
        max_left_elevation[wall_index] = max(max_left_elevation_so_far, max_left_elevation[wall_index - 1])

    max_right_elevation_so_far = elevation_map[-1]
    for wall_index in range(total_walls - 1, -1, -1):
        max_right_elevation[wall_index] = max(max_right_elevation_so_far, max_right_elevation[wall_index + 1])

