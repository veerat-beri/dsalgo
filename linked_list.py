from builtins import NotImplementedError


class _LinkedListNode:
    def __init__(self, data):
        self.data = data


class SinglyLinkedListNode(_LinkedListNode):
    def __init__(self, data):
        super(SinglyLinkedListNode, self).__init__(data)
        self.next = None


class DoublyLinkedListNode(SinglyLinkedListNode):
    def __init__(self, data):
        super(DoublyLinkedListNode, self).__init__(data)
        self.previous = None


class _LinkedList:
    def __init__(self, **kwargs):
        self.head = None

    def insert_at_begin(self, node: _LinkedListNode):
        raise NotImplementedError('func insert_at_begin() must be implemented')

    # def insert_at_end(self):
    #     raise NotImplementedError('func insert_at_end() must be implemented')

    def print_linked_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end='  ')
            current_node = current_node.next


class SinglyLinkedList(_LinkedList):
    def insert_at_begin(self, node: DoublyLinkedListNode):
        node.next = self.head
        self.head = node


class DoublyLinkedList(_LinkedList):
    def insert_at_begin(self, node: DoublyLinkedListNode):
        node.next = self.head
        self.head = node

    # def insert_at_end(self, node: Node):
    #     self.end.next = node
    #     self.end = node


class BuildLinkedList:
    def __init__(self, singly_linked_list=None, doubly_linked_list=None, list_of_nodes: [_LinkedListNode]=None):
        self.doubly_linked_list = doubly_linked_list
        self.singly_linked_list = singly_linked_list
        self.list_of_nodes = list_of_nodes

    def build(self):
        if not self.doubly_linked_list:
            self.doubly_linked_list = DoublyLinkedList()
        if not self.list_of_nodes:
            self.list_of_nodes = [Node(4), Node(6), Node(5)]

        for node in self.list_of_nodes:
            self.doubly_linked_list.insert_at_begin(node)

        return self.doubly_linked_list


# driver code
def run():
    list_of_nodes = [Node(1), Node(2), Node(3)]
    doubly_linked_list = BuildDoublyLinkedList(list_of_nodes=list_of_nodes).build()
    doubly_linked_list.print_linked_list()


if __name__ == '__main__':
    run()