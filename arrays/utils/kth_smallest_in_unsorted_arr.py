# Problem Statement
# https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/


from heaps.heap import MaxHeap, MinHeap
from sorting.quick_sort import get_pivot_index


def get_kth_smallest_num(arr: [], k, execution_method = 1):
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
    def _use_quick_search():
        print('Using Quick Search..')

        def _get_pivot_index(low, high):
            if low > high:
                return

            if k <= high and k >= low:
                pivot_index = get_pivot_index(arr, low, high)
                if pivot_index == k:
                    return arr[k]

                elif pivot_index < k:
                    return _get_pivot_index(pivot_index + 1, high)

                return _get_pivot_index(low, pivot_index - 1)

        return _get_pivot_index(0, arr_len - 1)

    method_to_use = {
        1: _use_min_heap,
        2: _use_max_heap,
        3: _use_quick_search,
    }

    executing_func = method_to_use[execution_method]
    return executing_func()


# driver code
def run():
    arr = [12, 3, 5, 7, 19, ]
    k = 2
    print(f'Given array: {arr} \n')
    print(f'Kth({k}) smallest num in given arr is: {get_kth_smallest_num(arr, k, 3)}')


if __name__ == '__main__':
    run()
