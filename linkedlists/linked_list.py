from builtins import NotImplementedError


class _LinkedListNodeMixin:
    class _LinkedListNode:
        def __init__(self, data, **kwargs):
            self._data = data

        @property
        def data(self):
            return self._data


class _LinkedList(_LinkedListNodeMixin):
    def __init__(self, head: _LinkedListNodeMixin._LinkedListNode = None, **kwargs):
        self.head = head

        # set tail node
        if self.head is not None:
            current_node = self.head
            while current_node:
                self.tail = current_node
                current_node = current_node.next
        else:
            self.tail = None

    def __len__(self):
        no_of_nodes_in_list = 0
        current_node = self.head
        while current_node:
            no_of_nodes_in_list += 1
            current_node = current_node.next

        return no_of_nodes_in_list

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

    def _set_head_tail(self, node):
        if not self.tail or not self.head:
            self.tail = node
            self.head = node

    def get_new_node(self, node_data):
        raise NotImplementedError('Has to be Implemented by sub class')

    def insert_at_begin(self, node: _LinkedListNodeMixin._LinkedListNode):
        raise NotImplementedError('Has to be Implemented by sub class')

    def insert_at_end(self, node: _LinkedListNodeMixin._LinkedListNode):
        raise NotImplementedError('Has to be Implemented by sub class')

    def remove(self, node: _LinkedListNodeMixin._LinkedListNode):
        raise NotImplementedError('Has to be Implemented by sub class')

    def is_empty(self):
        # Method 1
        # return len(self) == 0
        # Method 2
        return self.head is None

    def print_linked_list(self, with_address=False):
        current_node = self.head
        while current_node:
            print(current_node.data, f'({id(current_node)})' if with_address else '', end='  ', sep='')
            current_node = current_node.next
        print('\n')


class SinglyLinkedListNodeMixin(_LinkedListNodeMixin):
    class Node(_LinkedListNodeMixin._LinkedListNode):
        def __init__(self, data, **kwargs):
            super().__init__(data, **kwargs)
            self.next = None


class SinglyLinkedList(SinglyLinkedListNodeMixin, _LinkedList):
    @classmethod
    def get_new_node(cls, node_data):
        return cls.Node(node_data)

    def insert_at_begin(self, node_data):
        new_node = self.get_new_node(node_data)
        if self.is_empty():
            self._set_head_tail(new_node)
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, node_data):
        new_node = self.get_new_node(node_data)
        if self.is_empty():
            self._set_head_tail(new_node)
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, node: SinglyLinkedListNodeMixin.Node):
        pass


class DoublyLinkedListNodeMixin(SinglyLinkedListNodeMixin):
    class DoublyLinkedListNode(SinglyLinkedListNodeMixin.Node):
        def __init__(self, data, **kwargs):
            super().__init__(data, **kwargs)
            self.previous = None


class DoublyLinkedList(DoublyLinkedListNodeMixin, _LinkedList):
    def get_new_node(self, node_data):
        return self.DoublyLinkedListNode(node_data)

    def insert_at_begin(self, node_data=None, node: DoublyLinkedListNodeMixin.DoublyLinkedListNode = None):
        assert node or node_data, 'Data or node not provided to be inserted'

        new_node = node or self.get_new_node(node_data)
        if self.is_empty():
            self._set_head_tail(new_node)
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def insert_at_end(self, node_data):
        new_node = self.get_new_node(node_data)
        if self.is_empty():
            self._set_head_tail(new_node)
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

    def remove(self, node: DoublyLinkedListNodeMixin.DoublyLinkedListNode):
        if node.previous is None:  # node is head node
            self.head = node.next
        else:
            node.previous.next = node.next

        if node.next is None:  # node is tail node
            self.tail = node.previous
        else:
            node.next.previous = node.previous


# driver code
def run():
    from linkedlists.build_linked_list import BuildSinglyLinkedList
    print('Sample Linked List: ')
    singly_linked_list = BuildSinglyLinkedList(auto_populate=True).get_ll()

    singly_linked_list.print_linked_list()


if __name__ == '__main__':
    run()
