import heapq

from trees import LinkedBinaryTree


class _Heap:
    class HeapNode(LinkedBinaryTree.BinaryTreeNode):
        def __init__(self, data, left=None, right=None, **kwargs):
            super().__init__(data, left, right, **kwargs)

    def __init__(self, arr: []):
        self._size = len(arr)
        self._arr = arr or []
        self.heap = self._arr
        self.heapify()

    def __len__(self):
        return self._size

    def __str__(self):
        return self.heap

    def __repr__(self):
        return str(self.heap)

    def heapify(self):
        raise NotImplementedError('Has to be Implemented by sub class')

    def replace_root(self, elem: int):
        raise NotImplementedError('Has to be Implemented by sub class')

    def is_empty(self):
        return bool(self._size)

    def pop(self):
        self._size -= 1
        return heapq.heappop(self.heap)

    def get_parent(self, child_index):
        parent_index = (child_index - 1) // 2
        assert parent_index >= 0, 'No parent exists'
        return parent_index

    def get_left_child_index(self, parent_index):
        try:
            return self.heap[parent_index*2 + 1]
        except IndexError:
            print('Left Child don\'t exists')

    def get_right_child_index(self, parent_index):
        try:
            return self.heap[parent_index*2 + 2]
        except IndexError:
            print('Right Child don\'t exists')


class MinHeap(_Heap):
    def get_min(self):
        assert self.heap, 'Heap cannot be empty'
        return self.heap[0]

    def heapify(self):
        return heapq.heapify(self.heap)

    def replace_root(self, elem: int):
        heapq.heapreplace(self.heap, elem)


class MaxHeap(_Heap):
    def get_max(self):
        assert self.heap, 'Heap cannot be empty'
        return self.heap[0]

    def heapify(self):
        return heapq._heapify_max(self.heap)

    def replace_root(self, elem: int):
        heapq._heapreplace_max(self.heap, elem)

    # def heappop(self):
    #     return heapq
