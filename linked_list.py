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
        self.head = head if head else None
        self.tail = None

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
    def __init__(self, head: SinglyLinkedListNode=None, **kwargs):
        super(SinglyLinkedList, self).__init__(head, **kwargs)

    def set_head_tail(self, node):
        if not self.tail or not self.head:
            self.tail = node
            self.head = node
            return True
        return False

    def insert_at_begin(self, node: SinglyLinkedListNode):
        if not self.set_head_tail(node):
            node.next = self.head
            self.head = node

    def insert_at_end(self, node: SinglyLinkedListNode):
        if not self.set_head_tail(node):
            self.tail.next = node
            self.tail = node


class DoublyLinkedList(_LinkedList):
    def __init__(self, head: DoublyLinkedListNode=None, **kwargs):
        super(DoublyLinkedList, self).__init__(head, **kwargs)

    def insert_at_begin(self, node: DoublyLinkedListNode):
        node.next = self.head
        self.head.previous = node
        self.head = node


class _BuildLinkedList:
    def __init__(self, list_of_nodes: [_LinkedListNode]=None, auto_populate=True, **kwargs):
        self.auto_populate = auto_populate
        self.list_of_nodes = list_of_nodes + ([SinglyLinkedListNode(4), SinglyLinkedListNode(6), SinglyLinkedListNode(5)] if self.auto_populate else [])

    def build(self):
        raise NotImplementedError


class BuildSinglyLinkedList(_BuildLinkedList):
    def __init__(self, singly_linked_list=None, list_of_nodes: [DoublyLinkedListNode]=None, insert_at_end=True, auto_populate=True, **kwargs):
        super(BuildSinglyLinkedList, self).__init__(list_of_nodes, auto_populate, **kwargs)
        self.singly_linked_list = singly_linked_list
        self.insert_at_end = insert_at_end

    def build(self):
        if not self.singly_linked_list:
            self.singly_linked_list = SinglyLinkedList()

        function_to_use = 'insert_at_end' if self.insert_at_end else 'insert_at_begin'
        for node in self.list_of_nodes:
            self.singly_linked_list.__getattribute__(function_to_use)(node)

        return self.singly_linked_list


class BuildDoublyLinkedList(_BuildLinkedList):
    def __init__(self, doubly_linked_list=None, list_of_nodes: [DoublyLinkedListNode]=None, auto_populate=True, **kwargs):
        super(BuildDoublyLinkedList, self).__init__(list_of_nodes, auto_populate, **kwargs)
        self.doubly_linked_list = doubly_linked_list

    def build(self):
        if not self.doubly_linked_list:
            self.doubly_linked_list = DoublyLinkedList()
        if not self.list_of_nodes and self.auto_populate:
            self.list_of_nodes = [DoublyLinkedListNode(4), DoublyLinkedListNode(5), DoublyLinkedListNode(6)]

        for node in self.list_of_nodes:
            self.doubly_linked_list.insert_at_begin(node)

        return self.doubly_linked_list


# driver code
def run():
    list_of_nodes = [SinglyLinkedListNode(1), SinglyLinkedListNode(2), SinglyLinkedListNode(3)]
    singly_linked_list = BuildSinglyLinkedList(list_of_nodes=list_of_nodes, auto_populate=False).build()

    singly_linked_list.print_linked_list()


if __name__ == '__main__':
    run()