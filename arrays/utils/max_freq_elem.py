# Problem Statement
# https://www.geeksforgeeks.org/frequent-element-array/

import sys
from collections import defaultdict


class MaxFreq:
    def __init__(self, arr):
        self.arr = arr
        self.arr_len = len(arr)

    # Time Complexity: O(N*Log N + 2N)
    # Space Complexity: O(1)
    def _using_sorting(self):
        # Sort the array
        self.arr.sort()

        # Get max frequency
        arr_index = 0
        max_freq = 0

        while arr_index < self.arr_len:
            elem_freq = 1
            while arr_index < self.arr_len - 1 and self.arr[arr_index] == self.arr[arr_index + 1]:
                elem_freq += 1
                arr_index += 1
            arr_index += 1
            max_freq = max(max_freq, elem_freq)

        # Get all max frequency elements
        arr_index = 0

        while arr_index < self.arr_len:
            elem_freq = 1
            while arr_index < self.arr_len - 1 and self.arr[arr_index] == self.arr[arr_index + 1]:
                elem_freq += 1
                arr_index += 1
            if max_freq == elem_freq:
                yield self.arr[arr_index]
            arr_index += 1

    # Time Complexity: O(3N)
    # Space Complexity: O(N)
    def _using_hashing(self):
        freq_count = defaultdict(int)
        for elem in self.arr:
            freq_count[elem] += 1

        # Get max frequency
        max_freq = - sys.maxsize
        for elem in freq_count:
            elem_freq = freq_count[elem]
            if elem_freq > max_freq:
                max_freq = elem_freq

        # Get all max frequency elements
        for elem in freq_count:
            if freq_count[elem] == max_freq:
                yield elem

    def get_max_freq_elems(self, use_sorting=False):
        exec_method = self._using_sorting if use_sorting else self._using_hashing
        return exec_method()


# driver code
def run():
    # arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]
    arr = [1, 5, 2, 1, 3, 2, 1, 2, ]
    print(f'Given array: {arr}')
    max_freq_elems = MaxFreq(arr).get_max_freq_elems(True)
    print(f'Max freq elements are: {list(max_freq_elems)}')


if __name__ == '__main__':
    run()
