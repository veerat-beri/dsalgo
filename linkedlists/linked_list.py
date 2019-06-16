from builtins import NotImplementedError


class _LinkedListNodeMixin:
    class Node:
        def __init__(self, data, **kwargs):
            self._data = data

        @property
        def data(self):
            return self._data

        def reset(self, new_data=None):
            if new_data:
                self._data = new_data

    @classmethod
    def get_new_node(cls, node_data):
        return cls.Node(node_data)


class _BaseLinkedList:
    def __init__(self, head: _LinkedListNodeMixin.Node = None, **kwargs):
        self.head = head

        # set tail node
        if self.head is not None:
            current_node = self.head
            while current_node:
                self.tail = current_node
                current_node = current_node.next
        else:
            self.tail = None

        self._size = 0

    def __len__(self):
        ###############
        # Method 1
        return self._size
        ###############
        # Method 2
        # no_of_nodes_in_list = 0
        # for _ in self:
        #     no_of_nodes_in_list += 1
        # return no_of_nodes_in_list
        ###############

    def _set_head_tail(self, node):
        if not self.tail or not self.head:
            self.tail = node
            self.head = node

    def _insert(self, handle_insert_func, node_data=None, node: _LinkedListNodeMixin.Node = None):
        assert node or node_data, 'Either of Data or node must be provided'
        new_node = node or self.get_new_node(node_data)

        if self.is_empty():
            self._set_head_tail(new_node)
        else:
            handle_insert_func(new_node)
        self._size += 1

    def is_empty(self):
        ###############
        # Method 1
        # return len(self) == 0
        ###############
        # Method 2
        return self.head is None
        ###############


class _LinkedList(_BaseLinkedList, _LinkedListNodeMixin):
    def print_linked_list(self, with_address=False):
        current_node = self.head
        while current_node:
            print(current_node.data, f'({id(current_node)})' if with_address else '', end='  ', sep='')
            current_node = current_node.next
        print('\n')

    def insert_at_begin(self, node_data=None, node: _LinkedListNodeMixin.Node = None):
        self._insert(self._handle_insert_at_begin, node_data, node)

    def insert_at_end(self, node_data=None, node: _LinkedListNodeMixin.Node = None):
        self._insert(self._handle_insert_at_end, node_data, node)

    def _handle_insert_at_begin(self, new_node: _LinkedListNodeMixin.Node):
        raise NotImplementedError('Has to be Implemented by sub class')

    def _handle_insert_at_end(self, new_node: _LinkedListNodeMixin.Node):
        raise NotImplementedError('Has to be Implemented by sub class')

    def remove(self, node: _LinkedListNodeMixin.Node):
        raise NotImplementedError('Has to be Implemented by sub class')


class SinglyLinkedListIterMixin:
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next


class SinglyLinkedListNodeMixin(_LinkedListNodeMixin):
    class Node(_LinkedListNodeMixin.Node):
        def __init__(self, data, **kwargs):
            super().__init__(data, **kwargs)
            self.next = None

        def reset(self, new_data=None, reset_pointers: bool = False):
            super().reset(new_data)
            if reset_pointers:
                self.next = None


class SinglyLinkedList(_LinkedList, SinglyLinkedListNodeMixin, SinglyLinkedListIterMixin):
    def _handle_insert_at_begin(self, new_node: SinglyLinkedListNodeMixin.Node):
        new_node.next = self.head
        self.head = new_node

    def _handle_insert_at_end(self, new_node: SinglyLinkedListNodeMixin.Node):
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, node: SinglyLinkedListNodeMixin.Node):
        pass


class DoublyLinkedListNodeMixin(SinglyLinkedListNodeMixin):
    class Node(SinglyLinkedListNodeMixin.Node):
        def __init__(self, data, **kwargs):
            super().__init__(data, **kwargs)
            self.previous = None

        def reset(self, new_data=None, reset_pointers: bool = False):
            super().reset(new_data, reset_pointers)
            if reset_pointers:
                self.previous = None


class DoublyLinkedList(_LinkedList, DoublyLinkedListNodeMixin, SinglyLinkedListIterMixin):
    def _handle_insert_at_begin(self, new_node: SinglyLinkedListNodeMixin.Node):
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node

    def _handle_insert_at_end(self, new_node: SinglyLinkedListNodeMixin.Node):
        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node

    def remove(self, node: DoublyLinkedListNodeMixin.Node):
        if node.previous is None:  # node is head node
            self.head = node.next
        else:
            node.previous.next = node.next

        if node.next is None:  # node is tail node
            self.tail = node.previous
        else:
            node.next.previous = node.previous

        self._size -= 1


# driver code
def run():
    from linkedlists.build_linked_list import BuildSinglyLinkedList
    print('Sample Linked List: ')
    singly_linked_list = BuildSinglyLinkedList(auto_populate=True).get_ll()

    singly_linked_list.print_linked_list()


if __name__ == '__main__':
    run()
