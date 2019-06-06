# Problem Statement
# https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
from typing import List

from heaps.heap import MaxBinaryHeap


def get_sliding_window_max(window_size: int, arr: List[int]):
    # Using Heap
    def _get_sliding_window_max_using_heap():
        # Build Heap
        max_heap = MaxBinaryHeap(arr[:window_size])
        for arr_index in range(window_size, len(arr)):
            yield max_heap.pop()
            max_heap.push(arr[arr_index])



# driver code
def run():
    pass


if __name__ == '__main__':
    run()
