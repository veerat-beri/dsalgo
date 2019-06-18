from base.services import assert_only_one_arg_is_present
from linkedlists.mixins import SinglyLinkedListNodeMixin, SinglyLinkedListIterMixin, _LinkedListMixin, \
    DoublyLinkedListNodeMixin


class SinglyLinkedList(_LinkedListMixin, SinglyLinkedListNodeMixin, SinglyLinkedListIterMixin):
    def _handle_insert_at_begin(self, new_node: SinglyLinkedListNodeMixin.Node):
        new_node.next = self.head
        self.head = new_node

    def _handle_insert_at_end(self, new_node: SinglyLinkedListNodeMixin.Node):
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, node: SinglyLinkedListNodeMixin.Node = None, node_data=None):
        assert_only_one_arg_is_present('Either of Data or node must be provided', node, node_data)
        # args = iter([node, node_data])
        # assert any(args) and not any(args), 'Either of Data or node must be provided'

        previous_node = None
        node_found = False

        if node:
            for current_node in self:
                if current_node == node:
                    node_found = True
                    break
                previous_node = current_node
        else:
            for current_node in self:
                if current_node.data == node_data:
                    node_found = True
                    node = current_node
                    break
                previous_node = current_node

        if node_found:
            previous_node.next = node.next
            del node
            self._size -= 1
        else:
            raise Exception('Given node not found!')


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
