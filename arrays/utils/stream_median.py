# Problem Statement
# https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/

from heaps.heap import MinBinaryHeap, MaxBinaryHeap


class RunningStreamMedian:
    def __init__(self, arr: []):
        self.min_heap = MinBinaryHeap()
        self.max_heap = MaxBinaryHeap()
        self.arr = arr

    def __append_elem(self, elem: int, previous_median: int):
        are_heap_len_equal = True
        elem_inserted_in = self.max_heap

        if len(self.max_heap) > len(self.min_heap):
            if elem < previous_median:
                max_elem = self.max_heap.get_max()
                self.min_heap.push(max_elem)
                self.max_heap.replace_root(elem)
            else:
                self.min_heap.push(elem)
                elem_inserted_in = self.min_heap

        elif len(self.max_heap) < len(self.min_heap):
            if elem > previous_median:
                min_elem = self.min_heap.get_min()
                self.max_heap.push(min_elem)
                self.min_heap.replace_root(elem)
                elem_inserted_in = self.min_heap
            else:
                self.max_heap.push(elem)
        else:



            if elem > previous_median:
                self.min_heap.push(elem)
                elem_inserted_in = self.min_heap
            else:
                print('before push:', elem, self.min_heap, self.max_heap)
                self.max_heap.push(elem)
                print('after push:', self.max_heap)
                print(self.max_heap.get_max())

            print(elem_inserted_in.root)
            are_heap_len_equal = False

        return are_heap_len_equal, elem_inserted_in

    def get_median(self):
        median_so_far = 0
        for elem in self.arr:
            are_heap_len_equal, elem_inserted_in = self.__append_elem(elem, median_so_far)

            if are_heap_len_equal:
                median_so_far = (self.max_heap.get_max() + self.min_heap.get_min())/2
            else:
                median_so_far = elem_inserted_in.root

            yield median_so_far


# driver code
def run():
    # arr = [5, 10, 15, ]
    arr = [5, 15, 10, 20, 3, ]
    for median in RunningStreamMedian(arr).get_median():
        print(median)


if __name__ == '__main__':
    run()
