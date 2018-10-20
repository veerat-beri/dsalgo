# Problem Statement
# https://www.geeksforgeeks.org/reverse-a-linked-list/


from linkedlist import BuildSinglyLinkedList
from linkedlist.linked_list import SinglyLinkedList


######################################
# Iterative approach

def reverse_linked_list(linked_list: SinglyLinkedList):
    current_node = linked_list.head
    previous_node = None

    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node

    return previous_node

######################################
# Recursive Approach


# def reverse_linked_list(linked_list: SinglyLinkedList):
#     pass

######################################

# driver code
def run():
    singly_linked_list = BuildSinglyLinkedList(auto_populate=True).build()

    print('Linked List before reversal: ')
    singly_linked_list.print_linked_list()

    print('\n\nLinked List after reversal: ')
    new_head = reverse_linked_list(singly_linked_list)
    singly_linked_list.head = new_head
    singly_linked_list.print_linked_list()


if __name__ == '__main__':
    run()

