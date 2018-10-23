# Problem statement
# https://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/
from linkedlist import SinglyLinkedList, BuildSinglyLinkedList


def find_kth_node_from_end(singly_linked_list: SinglyLinkedList, k):
    len_of_list = len(singly_linked_list)
    current_node = singly_linked_list.head

    for _ in range(len_of_list - k):
        current_node = current_node.next

    return current_node


# driver code
def run():
    singly_linked_list = BuildSinglyLinkedList(auto_populate=True).build()
    k = 3

    print('Given Linked List: ')
    singly_linked_list.print_linked_list()

    required_node = find_kth_node_from_end(singly_linked_list, k)
    print('\n\nKth ode from end: ', required_node)




