from builtins import NotImplementedError


class _LinkedListNode:
    def __init__(self, data, **kwargs):
        self.data = data


class SinglyLinkedListNode(_LinkedListNode):
    def __init__(self, data, **kwargs):
        super(SinglyLinkedListNode, self).__init__(data, **kwargs)
        self.next = None


class DoublyLinkedListNode(SinglyLinkedListNode):
    def __init__(self, data, **kwargs):
        super(DoublyLinkedListNode, self).__init__(data, **kwargs)
        self.previous = None


class _LinkedList:
    def __init__(self, head: _LinkedListNode=None, **kwargs):
        self.head = head
        self.tail = None

    def _set_head_tail(self, node):
        if not self.tail or not self.head:
            self.tail = node
            self.head = node
            return True
        return False

    def insert_at_begin(self, node: _LinkedListNode):
        raise NotImplementedError('func insert_at_begin() must be implemented')

    def insert_at_end(self, node: _LinkedListNode):
        raise NotImplementedError('func insert_at_end() must be implemented')

    def print_linked_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end='  ')
            current_node = current_node.next


class SinglyLinkedList(_LinkedList):
    def __init__(self, head: SinglyLinkedListNode=None, **kwargs):
        super(SinglyLinkedList, self).__init__(head, **kwargs)

    def insert_at_begin(self, node: SinglyLinkedListNode):
        if not self._set_head_tail(node):
            node.next = self.head
            self.head = node

    def insert_at_end(self, node: SinglyLinkedListNode):
        if not self._set_head_tail(node):
            self.tail.next = node
            self.tail = node


class DoublyLinkedList(_LinkedList):
    def __init__(self, head: DoublyLinkedListNode=None, **kwargs):
        super(DoublyLinkedList, self).__init__(head, **kwargs)

    def insert_at_begin(self, node: DoublyLinkedListNode):
        if not self._set_head_tail(node):
            node.next = self.head
            self.head.previous = node
            self.head = node

    def insert_at_end(self, node: DoublyLinkedListNode):
        if not self._set_head_tail(node):
            self.tail.next = node
            node.previous = self.tail
            self.tail = node


# driver code
def run():
    from linkedlist.build_linked_list import BuildSinglyLinkedList

    list_of_nodes = [SinglyLinkedListNode(1), SinglyLinkedListNode(2), SinglyLinkedListNode(3)]
    singly_linked_list = BuildSinglyLinkedList(list_of_nodes=list_of_nodes, auto_populate=False).build()

    singly_linked_list.print_linked_list()


if __name__ == '__main__':
    run()
