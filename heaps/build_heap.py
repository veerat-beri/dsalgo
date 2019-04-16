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

    def get_min_child_index(self, parent_index):
        # Assuming parent has at least left-child
        left_child = self.get_left_child_index(parent_index)
        try:
            right_child = self.get_right_child(parent_index)
            return self.get_left_child_index(parent_index) if left_child < right_child else self.get_right_child_index(parent_index)
        except IndexError:
            return self.get_left_child_index(parent_index)

    def percolate_down(self, elem_index):
        while self.get_left_child_index(elem_index):
            min_child_index = self.get_min_child_index(elem_index)
            if self.heap[elem_index] < self.heap[min_child_index]:
                swap_arr_elem(elem_index, min_child_index, self.heap)
            elem_index = min_child_index

    def insert(self, elem: int):
        self.heap.append(elem)
        self._insert()

    def delete_min(self):
        self.heap[0] = self.heap[-1]
        self.heap
        t = list()
        t.

    def heapify(self):
        pass
