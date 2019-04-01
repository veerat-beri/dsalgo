import heapq

from trees import LinkedBinaryTree


class _Heap:
    class HeapNode(LinkedBinaryTree.BinaryTreeNode):
        def __init__(self, data, left=None, right=None, **kwargs):
            super().__init__(data, left, right, **kwargs)

    def __init__(self, arr: []):
        self._size = 0
        self.arr = arr
        self.heapify(self.arr)

    def __len__(self):
        return self._size

    def heapify(self):
        raise NotImplementedError('Has to be Implemented by sub class')

    def is_empty(self):
        return bool(self._size)

    def get_parent(self, child_index):
        return (child_index - 1) // 2

    def get_left_child_index(self, parent_index):
        try:
            return self.arr[parent_index*2 + 1]
        except IndexError:
            print('Left Child don\'t exists')

    def get_right_child_index(self, parent_index):
        try:
            return self.arr[parent_index*2 + 2]
        except IndexError:
            print('Right Child don\'t exists')


class MinHeap(_Heap):
    def get_min(self):
        assert self.arr, 'Heap cannot be empty'
        return self.arr[0]

    def heapify(self):
        return heapq.heapify(self.arr)

    def heappop(self):
        return heapq.heappop(self.arr)


class MaxHeap(_Heap):
    def get_max(self):
        assert self.arr, 'Heap cannot be empty'
        return self.arr[0]

    def heapify(self):
        return heapq._heapify_max(self.arr)

    def heappop(self):
        return heapq
