class LinkedStack:
    class _StackNode:
        def __init__(self, data):
            self.next = None
            self._data = data

        @property
        def data(self):
            return self._data

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        node = self._root
        while node:
            yield node
            node = node.next

    @property
    def top(self):
        if self._root:
            return self._root.data
        raise ValueError('Stack is empty!')

    def _create_node(self, node_data):
        return self._StackNode(node_data)

    def is_empty(self):
        # 1st Approach
        # return self.top is None
        ###############

        # 2nd Approach
        return len(self) == 0

    def push(self, node_data):
        new_node = self._create_node(node_data)
        new_node.next = self._root
        self._root = new_node
        self._size += 1

    def _pop(self):
        popped_node = self._root
        self._root = self._root.next
        self._size -= 1
        return popped_node

    def pop(self):
        if self.is_empty():
            raise ValueError('Can not perform pop() operation as stack is empty!')
        return self._pop().data

    def print_stack(self):
        for node in self:
            print(node.data, end=' ')

    def __repr__(self):
        return ', '.join([str(node.data) for node in self])


# driver code
def run():
    stack = LinkedStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.print_stack()


if __name__ == '__main__':
    run()
