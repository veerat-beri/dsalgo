import heapq

from arrays.services import swap_arr_elem


class _BinaryHeap:
    # class HeapNode(LinkedBinaryTree.BinaryTreeNode):
    #     def __init__(self, data, left=None, right=None, **kwargs):
    #         super().__init__(data, left, right, **kwargs)

    def __init__(self, arr: [] = None):
        self._size = len(arr)
        self.heap = self._get_heap(arr)
        self.heapify()

    def _get_heap(self, arr):
        return arr[:] if arr else []

    @property
    def parent(self):
        return

    def __len__(self):
        return self._size

    def __repr__(self):
        return str(self.heap)

    def heapify(self):
        raise NotImplementedError('Has to be Implemented by sub class')

    def replace_root(self, elem: int):
        raise NotImplementedError('Has to be Implemented by sub class')

    def is_empty(self):
        return not self._size

    def pop(self):
        self._size -= 1
        return heapq.heappop(self.heap)

    def push(self, elem):
        self._size += 1
        return heapq.heappush(self.heap, elem)

    @staticmethod
    def get_parent_index(child_index):
        return (child_index - 1) // 2

    @staticmethod
    def get_left_child_index(parent_index):
        return parent_index * 2 + 1

    @staticmethod
    def get_right_child_index(parent_index):
        return parent_index * 2 + 2

    def get_left_child(self, parent_index):
        try:
            return self.heap[self.get_left_child_index(parent_index)]
        except IndexError:
            print('Left Child doesn\'t exists')
            raise

    def get_right_child(self, parent_index):
        try:
            return self.heap[self.get_right_child_index(parent_index)]
        except IndexError:
            print('Right Child doesn\'t exists')
            raise

    def get_parent(self, child_index):
        try:
            return self.heap[self.get_parent(child_index)]
        except IndexError:
            print('Parent doesn\'t exists')
            raise

    @staticmethod
    def get_root_index():
        return 0

    @property
    def root(self):
        try:
            return self.heap[self.get_root_index()]
        except IndexError:
            print('Heap is Empty')
            raise


class MinBinaryHeap(_BinaryHeap):
    def get_min(self):
        assert len(self), 'Heap cannot be empty'
        return self.heap[self.get_root_index()]

    def heapify(self):
        return heapq.heapify(self.heap)

    def replace_root(self, elem: int):
        return heapq.heapreplace(self.heap, elem)


class MaxBinaryHeap(_BinaryHeap):
    def get_max(self):
        assert len(self), 'Heap cannot be empty'
        return self.heap[self.get_root_index()]

    def heapify(self):
        return heapq._heapify_max(self.heap)

    def replace_root(self, elem: int):
        return heapq._heapreplace_max(self.heap, elem)

    def replace_elem(self, heap_arr_index):
        assert heap_arr_index < len(self.heap), 'input arr-index out of bounds'
        replaced_elem = self.heap[heap_arr_index]
        self.heap[heap_arr_index] = self.heap[-1]
        heapq._siftup_max(self.heap, 0)
        return replaced_elem


class _ManualHeap(_BinaryHeap):
    def _get_heap(self, arr):
        return [0] + (arr or [])

    def _percolate_down(self, elem_index: int):
        raise NotImplementedError('Has to be Implemented by sub class')

    def _build_heap(self, elem_index: int):
        while elem_index:
            self._percolate_down(elem_index)
            elem_index -= 1

    def _pop(self):
        self.heap[self.get_root_index()] = self.heap[-1]
        self._size -= 1
        self.heap.pop()
        self._percolate_down(self.get_root_index())

    def _push(self):
        self._size += 1
        self._percolate_up(self._size)

    def replace_root(self, elem: int):
        self.heap[self.get_root_index()] = elem
        self._percolate_down(self.get_root_index())

    def _percolate_up(self, elem_index: int):
        while self.get_parent_index(elem_index):
            parent_index = self.get_parent_index(elem_index)
            if self._is_swap_needed(parent_index, elem_index):
                swap_arr_elem(parent_index, elem_index, self.heap)
            elem_index = parent_index

    def _is_swap_needed(self, parent_index, child_index):
        raise NotImplementedError('Has to be Implemented by sub class')

    @staticmethod
    def get_root_index():
        return 1

    @staticmethod
    def get_parent_index(child_index: int):
        return child_index // 2

    @staticmethod
    def get_left_child_index(parent_index: int):
        return parent_index * 2

    @staticmethod
    def get_right_child_index(parent_index: int):
        return parent_index * 2 + 1

    # def push(self, elem: int):
    def push(self, elem):
        self.heap.append(elem)
        self._push()

    def pop(self):
        if self.is_empty():
            print('Heap is empty')
            raise IndexError
        min_elem = self.root
        self._pop()
        return min_elem

    def heapify(self):
        self._build_heap(self.get_parent_index(len(self)))


class ManualMinHeap(_ManualHeap):
    def _is_swap_needed(self, parent_index, child_index):
        return self.heap[parent_index] > self.heap[child_index]

    def __get_min_child_index(self, parent_index: int):
        left_child = self.get_left_child(parent_index)
        right_child = self.get_right_child(parent_index)
        return self.get_left_child_index(
            parent_index) if left_child < right_child else self.get_right_child_index(parent_index)

    def _get_min_child_index(self, parent_index: int):
        # Assuming parent has at least left-child
        if self.get_right_child_index(parent_index) <= self._size:
            return self.__get_min_child_index(parent_index)
        return self.get_left_child_index(parent_index)

    def _percolate_down(self, elem_index: int):
        while self.get_left_child_index(elem_index) <= len(self):
            min_child_index = self._get_min_child_index(elem_index)
            if self._is_swap_needed(elem_index, min_child_index):
                swap_arr_elem(elem_index, min_child_index, self.heap)
            elem_index = min_child_index

    def get_min(self):
        assert len(self), 'Heap cannot be empty'
        return self.heap[self.get_root_index()]


class ManualMaxHeap(_ManualHeap):
    def _is_swap_needed(self, parent_index, child_index):
        return self.heap[parent_index] < self.heap[child_index]

    def __get_max_child_index(self, parent_index: int):
        left_child = self.get_left_child(parent_index)
        right_child = self.get_right_child(parent_index)
        return self.get_left_child_index(parent_index) if left_child > right_child else self.get_right_child_index(
            parent_index)

    def _get_max_child_index(self, parent_index: int):
        # Assuming parent has at least left-child
        if self.get_right_child_index(parent_index) <= self._size:
            return self.__get_max_child_index(parent_index)
        return self.get_left_child_index(parent_index)

    def _percolate_down(self, elem_index: int):
        while self.get_left_child_index(elem_index) <= len(self):
            max_child_index = self._get_max_child_index(elem_index)
            if self._is_swap_needed(elem_index, max_child_index):
                swap_arr_elem(elem_index, max_child_index, self.heap)
            elem_index = max_child_index

    def get_max(self):
        assert len(self), 'Heap cannot be empty'
        return self.heap[self.get_root_index()]


class CustomNodeMinHeap(ManualMinHeap):
    def _is_swap_needed(self, parent_index, child_index):
        return self.heap[parent_index].data > self.heap[child_index].data

    def __get_min_child_index(self, parent_index: int):
        left_child = self.get_left_child(parent_index)
        right_child = self.get_right_child(parent_index)
        return self.get_left_child_index(
            parent_index) if left_child.data < right_child.data else self.get_right_child_index(parent_index)
