# Problem Statement
# https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/
import heapq


def get_kth_smallest_num(arr: [], k):
    # Using Min Heap
    # Time-complexity: O(N + k*log k)
    heap = arr
    arr_len = len(arr)
    assert k <= arr_len, 'k can not be greater than arr-len'

    def _use_min_heap():
        heapq.heapify(heap)
        for _ in range(k - 1):
            heapq.heappop(heap)

        return heapq.heappop(heap)

    return _use_min_heap()

    # Using Max Heap (Optimised)
    # Time-complexity: O(k + (N-k)*log k)
    def _use_max_heap():
        heapq._heapify_max(heap)

        for elem in range(k, arr_len):
            if elem in ran

# driver code
def run():
    arr = [12, 3, 5, 7, 19, ]
    k = 2
    print(f'Given array: {arr} ')
    print(f'Kth({k}) smallest num in given arr is: {get_kth_smallest_num(arr, k)}')


if __name__ == '__main__':
    run()
