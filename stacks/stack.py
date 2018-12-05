class LinkedStack:
    class _StackNode:
        def __init__(self, data):
            self.next = None
            self._data = data

        @property
        def data(self):
            return self._data

    def __init__(self):
        self.root = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self.root is None

    def create_node(self, node_data):
        return self._StackNode(node_data)

    def push(self, node_data):
        new_node = self.create_node(node_data)
        new_node.next = self.root
        self.root = new_node
        self._size += 1

    def pop(self):
        if not self.is_empty():
            popped_node = self.root
            self.root = self.root.next
            self._size -= 1
            return popped_node

    def __iter__(self):
        node = self.root
        while node:
            yield node
            node = node.next

    def print_stack(self):
        for node in self:
            print(node.data, end=' ')


# driver code
def run():
    stack = LinkedStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.print_stack()


if __name__ == '__main__':
    run()