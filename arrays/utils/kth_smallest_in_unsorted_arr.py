# Problem Statement
# https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/


from heaps.heap import MaxHeap, MinHeap


def get_kth_smallest_num(arr: [], k, use_min_heap=False):
    # Using Min Heap
    # Time-complexity: O(N + k*log k)
    arr_len = len(arr)
    assert k <= arr_len, 'k can not be greater than arr-len'

    def _use_min_heap():
        print('Using MIN-Heap..')

        heap = MinHeap(arr)

        for _ in range(k - 1):
            heap.pop()

        return heap.pop()

    # Using Max Heap (OPTIMISED)
    # Time-complexity: O(k + (N-k)*log k)
    def _use_max_heap():
        print('Using MAX-Heap..')

        heap = MaxHeap(arr[:k])

        for arr_index in range(k, arr_len):
            elem = arr[arr_index]
            if elem < heap.get_max():
                heap.replace_root(elem)

        return heap.pop()

    # Using Quick Sort
    def _use_quick_sort():
        pass

    executing_func = _use_min_heap if use_min_heap is True else _use_max_heap
    return executing_func()


# driver code
def run():
    arr = [12, 3, 5, 7, 19, ]
    k = 2
    print(f'Given array: {arr} ')
    print(f'Kth({k}) smallest num in given arr is: {get_kth_smallest_num(arr, k, use_min_heap=False)}')


if __name__ == '__main__':
    run()
