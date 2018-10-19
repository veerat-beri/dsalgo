# Problem Statement
# https://www.geeksforgeeks.org/reverse-a-linked-list/

from linkedlist.linked_list import SinglyLinkedList


#############################################
# Iterative approach


# def reverse_linked_list(linked_list: SinglyLinkedList):
#     current_node = linked_list.head
#     previous_node = None
#
#     while current_node:
#         next_node = current_node.next
#         current_node.next = previous_node
#         previous_node = current_node
#         current_node = next_node
#
#     return current_node
#
#
# BuildSinglyLinkedList().build()

#############################################

# Recursive Approach


def reverse_linked_list(linked_list: SinglyLinkedList):
    pass