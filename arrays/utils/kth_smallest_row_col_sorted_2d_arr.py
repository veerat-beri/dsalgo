# Problem Statement
# https://www.geeksforgeeks.org/kth-smallest-element-in-a-row-wise-and-column-wise-sorted-2d-array-set-1/


from heaps.build_heap import CustomMinHeap


def get_kth_smallest_in_sorted_2d_arr(arr: [], k):
    assert arr, 'Array can not be empty'

    def _get_processed_row():
        heap_arr = [(arr[0][col_index], 0, col_index) for col_index in range(len(arr[0]))]
        return heap_arr

    heap = CustomMinHeap(_get_processed_row())
    kth_smallest_node = None
    for _ in range(k):
        kth_smallest_node = heap.pop()
        try:
            heap.push(arr[kth_smallest_node[1]][kth_smallest_node[2]])
        except IndexError:
            continue

    return kth_smallest_node


# driver code
def run():
    arr = [
        [10, 20, 30, 40, ],
        [15, 25, 35, 45, ],
        [24, 29, 37, 48, ],
        [32, 33, 39, 50, ],
    ]
    k = 7
    kth_smallest_node = get_kth_smallest_in_sorted_2d_arr(arr, k)
    if kth_smallest_node:
        print(f'Kth({k}) smallest elem in given sorted 2D arr is: {kth_smallest_node[0]}')
    else:
        print('No Kth({k}) smallest elem exists')


if __name__ == '__main__':
    run()
