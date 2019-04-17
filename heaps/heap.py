import heapq


class _BinaryHeap:
    # class HeapNode(LinkedBinaryTree.BinaryTreeNode):
    #     def __init__(self, data, left=None, right=None, **kwargs):
    #         super().__init__(data, left, right, **kwargs)

    def __init__(self, arr: [] = None):
        arr = arr[:] if arr else []
        self._size = len(arr)

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
        return bool(self._size)

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
        return 1

    @property
    def root(self):
        try:
            return self.heap[self.get_root_index()]
        except IndexError:
            print('Heap is Empty')
            raise


class MinBinaryHeap(_BinaryHeap):
    def __init__(self, arr: [] = None):
        super(MinBinaryHeap, self).__init__(arr)
        self._size = len(arr)
        self.heap = arr[:]
        self._arr = arr[:]
        self.heapify()

    def get_min(self):
        assert self.heap, 'Heap cannot be empty'
        return self.heap[0]

    def heapify(self):
        return heapq.heapify(self.heap)

    def replace_root(self, elem: int):
        heapq.heapreplace(self.heap, elem)


class MaxBinaryHeap(_BinaryHeap):
    def get_max(self):
        assert self.heap, 'Heap cannot be empty'
        return self.heap[0]

    def heapify(self):
        return heapq._heapify_max(self.heap)

    def replace_root(self, elem: int):
        heapq._heapreplace_max(self.heap, elem)
