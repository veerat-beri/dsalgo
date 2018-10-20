from linkedlist import DoublyLinkedListNode, SinglyLinkedListNode, SinglyLinkedList, DoublyLinkedList
from linkedlist.linked_list import _LinkedList, _LinkedListNode


class _BuildLinkedList:
    def __init__(self, linked_list: _LinkedList=None, list_of_nodes: [_LinkedListNode]=[], insert_at_end=True, auto_populate=False, **kwargs):
        self.auto_populate = auto_populate
        self.list_of_nodes = list_of_nodes
        self.insert_at_end = insert_at_end
        self._linked_list = linked_list

        self._create_linked_list()
        self._create_list_of_nodes()

    def _create_linked_list(self):
        raise NotImplementedError

    def _create_list_of_nodes(self):
        raise NotImplementedError

    def build(self):
        insertion_scheme = 'insert_at_end' if self.insert_at_end else 'insert_at_begin'
        for node in self.list_of_nodes:
            getattr(self._linked_list, insertion_scheme)(node)

        return self._linked_list


class BuildSinglyLinkedList(_BuildLinkedList):
    def __init__(self, singly_linked_list=None, list_of_nodes: [DoublyLinkedListNode]=[], insert_at_end=True, auto_populate=False, **kwargs):
        super(BuildSinglyLinkedList, self).__init__(singly_linked_list, list_of_nodes, insert_at_end, auto_populate, **kwargs)

    def _create_list_of_nodes(self):
        self.list_of_nodes += [
            SinglyLinkedListNode(10), SinglyLinkedListNode(20), SinglyLinkedListNode(30),
            SinglyLinkedListNode(40), SinglyLinkedListNode(50),
        ] if self.auto_populate else []

    def _create_linked_list(self):
        if not self._linked_list:
            self._linked_list = SinglyLinkedList()


class BuildDoublyLinkedList(_BuildLinkedList):
    def __init__(self, doubly_linked_list=None, list_of_nodes: [DoublyLinkedListNode]=[], insert_at_end=True, auto_populate=False, **kwargs):
        super(BuildDoublyLinkedList, self).__init__(doubly_linked_list, list_of_nodes, insert_at_end, auto_populate, **kwargs)

    def _create_list_of_nodes(self):
        self.list_of_nodes += [
            DoublyLinkedListNode(10), DoublyLinkedListNode(20), DoublyLinkedListNode(30),
            DoublyLinkedListNode(40), DoublyLinkedListNode(50),
        ] if self.auto_populate else []

    def _create_linked_list(self):
        if not self._linked_list:
            self._linked_list = DoublyLinkedList()


class BuildSinglyLinkedListWithLoop(BuildSinglyLinkedList):
    def build(self):
        super(BuildSinglyLinkedListWithLoop, self).build()
        if self._linked_list.head and self._linked_list.tail:
            loop_start_elem = self._linked_list.head
            if loop_start_elem.next:
                loop_start_elem = loop_start_elem.next
                if loop_start_elem.next:
                    loop_start_elem = loop_start_elem.next

            self._linked_list.tail.next = loop_start_elem
        return self._linked_list