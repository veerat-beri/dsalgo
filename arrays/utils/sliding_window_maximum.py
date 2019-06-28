# Problem Statement
# https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/


from collections import deque
from typing import List


class SlidingWindowMax:
    def __init__(self, arr: List[int], window_size: int):
        self.window_size = window_size
        self.arr = arr
        self.arr_len = len(arr)

    # Time Complexity: O((K + LogK)*(N - K + 1))
    def _get_sliding_window_max_using_heap(self):
        pass

    # Time Complexity: O(K*(N - K + 1))
    def _using_naive_two_nested_loops(self):
        pass

    # Time Complexity: O(2N)
    def _get_sliding_window_max_using_deque(self):
        current_window_useful_elem_indexes = deque()
        """
        current_window_useful_elem_indexes saves useful elements' indexes in ascending order of their value.
        For e.g for arr= [8, 5, 10, 7, 9, 4, 15, 12, 90, 13] and k=4,
        It would be:
        - [3, 2] for 1st window (7, 10)
        - [4, 2] for 2nd window (9, 10) and so on
        """
        for arr_index in range(self.window_size):
            while current_window_useful_elem_indexes and self.arr[arr_index] > self.arr[current_window_useful_elem_indexes[0]]:
                current_window_useful_elem_indexes.popleft()
            current_window_useful_elem_indexes.appendleft(arr_index)

        for arr_index in range(self.window_size, self.arr_len):
            yield self.arr[current_window_useful_elem_indexes[-1]]
            removing_elem_index = arr_index - self.window_size
            while current_window_useful_elem_indexes and removing_elem_index >= current_window_useful_elem_indexes[-1]:
                current_window_useful_elem_indexes.pop()

            while current_window_useful_elem_indexes and self.arr[arr_index] > self.arr[current_window_useful_elem_indexes[0]]:
                current_window_useful_elem_indexes.popleft()
            current_window_useful_elem_indexes.appendleft(arr_index)

        yield self.arr[current_window_useful_elem_indexes[-1]]

    def get_sliding_window_max(self, **kwargs):
        if kwargs.get('use_deque'):
            return self._get_sliding_window_max_using_deque()
        else:
            return self._get_sliding_window_max_using_deque()


# driver code
def run():
    # arr = [1, 2, 3, 1, 4, 5, 2, 3, 6, ]
    # window_size = 3
    arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
    window_size = 4
    print(f'Given Array: {arr}')
    print(f'Greatest elem in each subarray of window size={window_size}, are: ')

    for elem in SlidingWindowMax(arr, window_size).get_sliding_window_max():
        print(elem, end=' ')


if __name__ == '__main__':
    run()
