# Problem Statement
# https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/


from heaps.heap import ManualMinHeap, ManualMaxHeap
from sorting.quick_sort import get_pivot_index


class KthSmallestElem:
    USE_MIN_HEAP = '_use_min_heap'
    USE_MAX_HEAP = '_use_max_heap'
    USE_QUICK_SEARCH = '_use_quick_search'

    def __init__(self, arr: [], k, execution_method=USE_MAX_HEAP):
        self.exec_func = getattr(self, execution_method)
        self.arr = arr
        self.arr_len = len(arr)
        self.k = k

    # Using Min Heap
    # Time-complexity: O(N + k*log2 N)
    def _use_min_heap(self):
        print('Using MIN-Heap..')
        heap = ManualMinHeap(self.arr)

        for _ in range(self.k - 1):
            heap.pop()

        return heap.pop()

    # Using Max Heap (OPTIMISED)
    # Time-complexity: O(k + (N-k) * log2 k)
    def _use_max_heap(self):
        print('Using MAX-Heap..')
        heap = ManualMaxHeap(self.arr[:self.k])

        for arr_index in range(self.k, self.arr_len):
            elem = self.arr[arr_index]
            if elem < heap.get_max():
                heap.replace_root(elem)

        return heap.pop()

    # Using Quick Sort partition method
    # Time-complexity:
    # - O(N^2) Worst case
    # - O(N) Avg. case
    def _use_quick_search(self):
        print('Using Quick Search..')
        k_index = self.k - 1

        def _get_pivot_index(low, high):
            if low > high:
                return

            if k_index <= high and k_index >= low:
                pivot_index = get_pivot_index(self.arr, low, high)
                if pivot_index == k_index:
                    return self.arr[k_index]

                elif pivot_index < k_index:
                    return _get_pivot_index(pivot_index + 1, high)

                return _get_pivot_index(low, pivot_index - 1)

        return _get_pivot_index(0, self.arr_len - 1)

    def get_kth_smallest_num(self):
        assert self.k <= self.arr_len, 'k can not be greater than sorted_arrays-len'
        return self.exec_func()


# driver code
def run():
    # arr = [12, 3, 21, 7, 19, ]
    arr = [12, 3, 5, 7, 19, ]
    k = 2
    print(f'Given array: {arr} \n')
    print(f'Kth({k}) smallest num in given arr is:\n')

    print(KthSmallestElem(arr, k, KthSmallestElem.USE_MIN_HEAP).get_kth_smallest_num())
    print(KthSmallestElem(arr, k, KthSmallestElem.USE_MAX_HEAP).get_kth_smallest_num())
    print(KthSmallestElem(arr, k, KthSmallestElem.USE_QUICK_SEARCH).get_kth_smallest_num())


if __name__ == '__main__':
    run()
