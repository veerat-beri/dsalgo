# Problem Statement
# https://leetcode.com/problems/container-with-most-water/
from typing import List


def get_max_area(height: List[int]) -> int:
    end_ptr = len(height) - 1
    start_ptr = 0
    max_area = 0

    while start_ptr < end_ptr:
        max_area = max(max_area, min(height[start_ptr], height[end_ptr]) * (end_ptr - start_ptr))

        if height[start_ptr] < height[end_ptr]:
            start_ptr += 1

        else:
            end_ptr -= 1

    return max_area


# driver code
def run():
    height_arr = [4, 3, 2, 1, 4]
    print("Max area for given height array: ", get_max_area(height_arr))


if __name__ == '__main__':
    run()
