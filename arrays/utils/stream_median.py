# Problem Statement
# https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/
from heaps.heap import MinBinaryHeap, MaxBinaryHeap


class RunningStreamMedian:
    def __init__(self, arr: []):
        self.min_heap = MinBinaryHeap()
        self.max_heap = MaxBinaryHeap()
        self.arr = arr

    def __append_elem(self, elem: int, previous_median: int):

        if len(self.max_heap) > len(self.min_heap) and elem < previous_median:
            max_elem = self.max_heap.get_max()
            self.min_heap.push(max_elem)
            self.max_heap.replace_root(elem)

    def get_median(self):
        # for elem in self.arr:
        pass


# driver code
def run():
    pass


if __name__ == '__main__':
    run()
