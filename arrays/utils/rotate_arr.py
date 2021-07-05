# Problem Statement
# https://leetcode.com/problems/rotate-array/

from typing import List
from mathematical.school_problems import get_gcd


class RotateArray:
    USING_JUGGLING = 'using_juggling'
    USING_ROTATION = 'using_rotation'

    def __init__(self, total_rotations: int, arr_len: int, method=USING_ROTATION):
        self.total_rotations = total_rotations
        self.arr_len = arr_len
        self.method = method

    @staticmethod
    def __reverse_arr(arr, start_index: int, end_index: int):
        while start_index < end_index:
            arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
            start_index += 1
            end_index -= 1

    # Using Array Rotation
    # Time Complexity: O(2N) ~= O(N)
    # Space Complexity: O(1) as using inplace rotation
    # https://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/
    def _using_arr_reversal(self, arr):
        if self.total_rotations == 0:
            return
        self.__reverse_arr(arr, 0, self.total_rotations - 1)
        self.__reverse_arr(arr, self.total_rotations, self.arr_len - 1)
        self.__reverse_arr(arr, 0, self.arr_len - 1)

    def rotate_arr(self, arr: []):
        assert arr, 'Array could not be empty'
        handling_method = self._using_juggling_algo if self.method == self.USING_JUGGLING else self._using_arr_reversal
        return handling_method(arr)

    # Efficient Juggling Algorithm
    # Time Complexity: O(N) OR O( gcd(n, d)*(n//d + 1) )
    # Space Complexity: O(1)
    # https://www.geeksforgeeks.org/array-rotation/
    def _using_juggling_algo(self, arr):
        for rotation_set_index in range(get_gcd(self.arr_len, self.total_rotations)):
            set_first_rotated_elem = arr[rotation_set_index]
            previous_rotated_index = rotation_set_index
            while 1:
                next_rotating_index = self.total_rotations + previous_rotated_index
                if next_rotating_index >= self.arr_len:
                    next_rotating_index = next_rotating_index - self.arr_len
                if next_rotating_index == rotation_set_index:
                    break

                arr[previous_rotated_index] = arr[next_rotating_index]
                previous_rotated_index = next_rotating_index

            arr[previous_rotated_index] = set_first_rotated_elem
        return arr


# driver code
def run():
    arr = [1, 2, 3, 4, 5, 6, 7]
    total_rotations = 2
    print(f'Given arr: {arr}')
    RotateArray(total_rotations, len(arr)).rotate_arr(arr)
    print(f'New arr after {total_rotations} rotations is:', arr)


if __name__ == '__main__':
    run()
