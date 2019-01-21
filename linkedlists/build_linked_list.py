from linkedlists.linked_list import SinglyLinkedList, DoublyLinkedList


class _BuildLinkedList:
    def __init__(self, list_of_nodes: [int]=None, insert_at_end=True, auto_populate=False, **kwargs):
        self.insert_at_end = insert_at_end
        self._linked_list = self._get_ll_instance()

        self.list_of_nodes = self._get_list_of_nodes(list_of_nodes, auto_populate)

    def _get_list_of_nodes(self, list_of_nodes, auto_populate):
        if list_of_nodes is None:
            list_of_nodes = []
        return ([10, 20, 30, 40, 50, ] if auto_populate else []) + list_of_nodes

    def _get_ll_instance(self):
        raise NotImplementedError('Has to be Implemented by sub class')

    def _build(self):
        insertion_scheme = 'insert_at_end' if self.insert_at_end else 'insert_at_begin'
        for node in self.list_of_nodes:
            getattr(self._linked_list, insertion_scheme)(node)

    def get_ll(self):
        self._build()
        return self._linked_list


class BuildSinglyLinkedList(_BuildLinkedList):
    def _get_ll_instance(self):
        return SinglyLinkedList()


class BuildDoublyLinkedList(_BuildLinkedList):
    def _get_ll_instance(self):
        return DoublyLinkedList()


class BuildSinglyLinkedListWithLoop(BuildSinglyLinkedList):
    def _build(self):
        # For sample LL: 10-> 20-> 30-> 40-> 50
        #
        # Returns: 10-> 20-> 30-> 40-> 50->
        #                    ^             |
        #                    |             |
        #                     <----<----<--
        #
        super(BuildSinglyLinkedListWithLoop, self)._build()
        if self._linked_list.head and self._linked_list.tail:
            loop_start_elem = self._linked_list.head
            if loop_start_elem.next:
                loop_start_elem = loop_start_elem.next
                if loop_start_elem.next:
                    loop_start_elem = loop_start_elem.next

            self._linked_list.tail.next = loop_start_elem