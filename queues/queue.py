from linkedlists.mixins import SinglyLinkedListIterMixin, SinglyLinkedListNodeMixin, _BaseLinkedListMixin


class LinkedQueue(_BaseLinkedListMixin, SinglyLinkedListIterMixin, SinglyLinkedListNodeMixin):
    @property
    def front(self):
        if not self.is_empty():
            return self._head.data
        raise ValueError('Stack is empty!')

    @property
    def rear(self):
        if not self.is_empty():
            return self._tail.data
        raise ValueError('Stack is empty!')

    def _handle_insert_at_end(self, new_node: SinglyLinkedListNodeMixin.Node):
        self.tail.next = new_node
        self.tail = new_node

    def enqueue(self, node_data):
        new_node = self.get_new_node(node_data)
        new_node.next = self._root
        self._root = new_node
        self._size += 1

    def _pop(self):
        if not self.is_empty():
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
