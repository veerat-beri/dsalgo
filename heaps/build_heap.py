from arrays.services import swap_arr_elem
from heaps.heap import MinBinaryHeap


class CustomMinHeap(MinBinaryHeap):
    def __init__(self, arr: []):
        # arr = arr if arr else []
        self._size = 0
        self.heap = [0]
        # self.heapify()

    def _insert(self):
        self._size += 1
        self.percolate_up(self._size)

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

    @staticmethod
    def get_parent_index(child_index):
        return child_index // 2

    @staticmethod
    def get_left_child_index(parent_index):
        return parent_index * 2

    @staticmethod
    def get_right_child_index(parent_index):
        return parent_index * 2 + 1

    def percolate_up(self, elem_index):
        parent_index = self.get_parent_index(elem_index)

        while parent_index:
            if self.heap[parent_index] < self.heap[elem_index]:
                swap_arr_elem(parent_index, elem_index, self.heap)
            parent_index = self.get_parent_index(parent_index)

    def get_min_child(self, parent_index):
        # Assuming parent has atleast one child
        pass

    def percolate_down(self, elem_index):
        pass

    def insert(self, elem: int):
        self.heap.append(elem)
        self._insert()

    def heapify(self):
        pass
