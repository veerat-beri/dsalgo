from linkedlists.mixins import SinglyLinkedListNodeMixin, SinglyLinkedListIterMixin, _LinkedListMixin, \
    DoublyLinkedListNodeMixin


class SinglyLinkedList(_LinkedListMixin, SinglyLinkedListNodeMixin, SinglyLinkedListIterMixin):
    def _handle_insert_at_begin(self, new_node: SinglyLinkedListNodeMixin.Node):
        new_node.next = self.head
        self.head = new_node

    def _handle_insert_at_end(self, new_node: SinglyLinkedListNodeMixin.Node):
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, node: SinglyLinkedListNodeMixin.Node):
        pass


class DoublyLinkedList(_LinkedListMixin, DoublyLinkedListNodeMixin, SinglyLinkedListIterMixin):
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
