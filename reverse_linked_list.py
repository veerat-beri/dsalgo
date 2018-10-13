from linked_list import DoublyLinkedList, Node, BuildDoublyLinkedList



# Iterative approach
def reverse_linked_list(linked_list: DoublyLinkedList):
    current_node = linked_list.head
    previous_node = None

    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node

    return current_node

BuildDoublyLinkedList([]).build()

