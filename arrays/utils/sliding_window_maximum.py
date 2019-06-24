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
        # Build Heap
        # max_heap = MaxBinaryHeap(arr[:window_size])
        # for arr_index in range(window_size, len(arr)):
        #     yield max_heap.pop()
        #     max_heap.push(arr[arr_index])
        pass

    # Time Complexity: O(K*(N - K + 1))
    def _using_naive_two_nested_loops(self):
        pass

    def get_sliding_window_max_using_deque(self):
        current_window_useful_elem_indexes = deque()
        for arr_index in range(self.window_size):
            while current_window_useful_elem_indexes and self.arr[arr_index] > self.arr[current_window_useful_elem_indexes[0]]:
                current_window_useful_elem_indexes.popleft()
            current_window_useful_elem_indexes.appendleft(arr_index)

        for arr_index in range(self.window_size, self.arr_len):



            print(current_window_useful_elem_indexes)
            yield self.arr[current_window_useful_elem_indexes[-1]]
            removing_elem_index = arr_index - self.window_size
            while current_window_useful_elem_indexes and removing_elem_index >= current_window_useful_elem_indexes[-1]:
                current_window_useful_elem_indexes.pop()

            while current_window_useful_elem_indexes and self.arr[arr_index] > self.arr[current_window_useful_elem_indexes[0]]:
                current_window_useful_elem_indexes.popleft()
            current_window_useful_elem_indexes.appendleft(arr_index)

        yield self.arr[current_window_useful_elem_indexes[-1]]


# driver code
def run():
    # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ]
    arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
    window_size = 3
    print(f'Given Array: {arr}')
    print(f'Window size: {window_size}')
    for elem in SlidingWindowMax(arr, window_size).get_sliding_window_max_using_deque():
        print(elem, end=' ')


if __name__ == '__main__':
    run()
