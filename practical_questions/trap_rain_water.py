# Problem Statement
# https://www.geeksforgeeks.org/trapping-rain-water/


def get_trapped_water_volume(elevation_map):
    #############################################
    # Time-complexity: O(3n)
    # Space-complexity: O(2n)

    total_walls = len(elevation_map)
    max_left_elevation = [0]*total_walls
    max_right_elevation = [0]*total_walls

    max_left_elevation[0] = elevation_map[0]
    for wall_index in range(1, total_walls):
        max_left_elevation[wall_index] = max(elevation_map[wall_index], max_left_elevation[wall_index - 1])

    max_right_elevation[-1] = elevation_map[-1]
    for wall_index in range(total_walls - 2, -1, -1):
        max_right_elevation[wall_index] = max(elevation_map[wall_index], max_right_elevation[wall_index + 1])

    total_trapped_water = 0
    for wall_index in range(total_walls):
        total_trapped_water += min(max_left_elevation[wall_index], max_right_elevation[wall_index]) - elevation_map[wall_index]

    return total_trapped_water

    #############################################
    # Space Optimized Solution


# driver code
def run():
    elevation_map = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # elevation_map = [3, 0, 0, 2, 0, 4]
    print(f'Given Elevation map: {elevation_map}')
    print(f'Total Water volume that could be trapped: {get_trapped_water_volume(elevation_map)}')


if __name__ == '__main__':
    run()

