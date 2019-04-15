from heaps.heap import MinBinaryHeap


class CustomMinHeap(MinBinaryHeap):
    def __init__(self, arr: []):
        # arr = arr if arr else []
        self._size = 0
        self.heap = [0]
        # self.heapify()

    # def heapify(self):
    #     pass

    # def replace_root(self, elem: int):
    #     pass

    def is_empty(self):
        return bool(self._size)

    # def pop(self):
    #     self._size -= 1
    #     return heapq.heappop(self.heap)

    # def push(self, elem):
    #     self._size += 1
    #     return heapq.heappush(self.heap, elem)

    def get_parent_index(self, child_index):
        # parent_index = child_index // 2
        # assert parent_index >= 0, 'No parent exists'
        return child_index // 2

    @staticmethod
    def get_left_child_index(parent_index):
        return parent_index * 2

    @staticmethod
    def get_right_child_index(parent_index):
        return parent_index * 2 + 1

    def percolate_up(self, elem_index):
        while self.get_parent_index(elem_index):
            if self._arr[parent_index] < self._arr[elem_index]:
                self._arr[parent_index], self._arr[elem_index] = self._arr[elem_index], self._arr[parent_index]
                self.percolate_up(parent_index)

    def heapify(self):
        pass
