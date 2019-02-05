from builtins import NotImplementedError


class _LinkedList:
    class _LinkedListNode:
        def __init__(self, data, **kwargs):
            self.data = data

    def __init__(self, head: _LinkedListNode=None, **kwargs):
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

    def _set_head_tail(self, node):
        if not self.tail or not self.head:
            self.tail = node
            self.head = node

    def _get_new_node(self, node_data):
        raise NotImplementedError('Has to be Implemented by sub class')

    def insert_at_begin(self, node: _LinkedListNode):
        raise NotImplementedError('Has to be Implemented by sub class')

    def insert_at_end(self, node: _LinkedListNode):
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


class SinglyLinkedList(_LinkedList):
    class SinglyLinkedListNode(_LinkedList._LinkedListNode):
        def __init__(self, data, **kwargs):
            super().__init__(data, **kwargs)
            self.next = None

    def _get_new_node(self, node_data):
        return self.SinglyLinkedListNode(node_data)

    def insert_at_begin(self, node_data):
        new_node = self._get_new_node(node_data)
        if self.is_empty():
            self._set_head_tail(new_node)
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, node_data):
        new_node = self._get_new_node(node_data)
        if self.is_empty():
            self._set_head_tail(new_node)
        else:
            self.tail.next = new_node
            self.tail = new_node


class DoublyLinkedList(_LinkedList):
    class DoublyLinkedListNode(SinglyLinkedList.SinglyLinkedListNode):
        def __init__(self, data, **kwargs):
            super().__init__(data, **kwargs)
            self.previous = None

    def _get_new_node(self, node_data):
        return self.DoublyLinkedListNode(node_data)

    def insert_at_begin(self, node_data):
        new_node = self._get_new_node(node_data)
        if self.is_empty():
            self._set_head_tail(new_node)
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def insert_at_end(self, node_data):
        new_node = self._get_new_node(node_data)
        if self.is_empty():

            print('is empty')
            self._set_head_tail(new_node)
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node


# driver code
def run():
    from linkedlists.build_linked_list import BuildSinglyLinkedList
    singly_linked_list = BuildSinglyLinkedList(auto_populate=True).get_ll()

    singly_linked_list.print_linked_list()


if __name__ == '__main__':
    run()
