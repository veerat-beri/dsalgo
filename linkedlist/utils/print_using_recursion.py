from linkedlist.linked_list import Node, BuildDoublyLinkedList


def recursively_print_linked_list(current_node: Node):
    if current_node:
        print(current_node.data, end='  ')
        recursively_print_linked_list(current_node.next)


doubly_linked_list = BuildDoublyLinkedList().build()
recursively_print_linked_list(doubly_linked_list.head)
