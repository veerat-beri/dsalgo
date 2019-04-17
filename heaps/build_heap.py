from arrays.services import swap_arr_elem
from heaps.heap import MinBinaryHeap


class ManualMinHeap(MinBinaryHeap):
    def __init__(self, arr: [] = None):
        self._size = len(arr)
        self.heap = [0] + (arr or [])

    def _push(self):
        self._size += 1
        self._percolate_up(self._size)

    # def replace_root(self, elem: int):
    #     pass

    @staticmethod
    def get_parent_index(child_index: int):
        return child_index // 2

    @staticmethod
    def get_left_child_index(parent_index: int):
        return parent_index * 2

    @staticmethod
    def get_right_child_index(parent_index: int):
        return parent_index * 2 + 1

    def _percolate_up(self, elem_index: int):
        parent_index = self.get_parent_index(elem_index)
        while parent_index:
            if self.heap[parent_index] > self.heap[elem_index]:
                swap_arr_elem(parent_index, elem_index, self.heap)
            parent_index = self.get_parent_index(parent_index)

    def _get_min_child_index(self, parent_index: int):
        # Assuming parent has at least left-child
        left_child = self.get_left_child_index(parent_index)
        try:
            right_child = self.get_right_child(parent_index)
            return self.get_left_child_index(parent_index) if left_child < right_child else self.get_right_child_index(parent_index)
        except IndexError:
            return self.get_left_child_index(parent_index)

    def _percolate_down(self, elem_index: int):
        while self.get_left_child_index(elem_index) <= len(self):
            min_child_index = self._get_min_child_index(elem_index)
            if self.heap[elem_index] > self.heap[min_child_index]:
                swap_arr_elem(elem_index, min_child_index, self.heap)
            elem_index = min_child_index

    def push(self, elem: int):
        self.heap.append(elem)
        self._push()

    def _pop(self):
        self.heap[0] = self.heap[-1]
        self._size -= 1
        self.heap.pop()
        self._percolate_down(self.get_root_index())

    def pop(self):
        if self.is_empty():
            print('Heap is empty')
            raise IndexError
        min_elem = self.root
        self._pop()
        return min_elem

    def _build_heap(self, elem_index: int):
        while elem_index:
            self._percolate_down(elem_index)
            elem_index -= 1

    def heapify(self):
        self._build_heap(self.get_parent_index(len(self)))
