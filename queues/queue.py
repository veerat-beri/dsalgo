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
        self._insert(self._handle_insert_at_end, node_data)

    def _pop(self):
        popped_node = self.head
        self.head = self.head.next
        self._size -= 1
        return popped_node

    def pop(self):
        if self.is_empty():
            raise ValueError('Can not perform pop() operation as stack is empty!')
        return self._pop().data

    def print_q(self):
        for node in self:
            print(node.data, end=' ')

    def __repr__(self):
        return ', '.join([str(node.data) for node in self])
