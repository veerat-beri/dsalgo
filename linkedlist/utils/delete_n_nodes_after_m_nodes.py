# Problem Statement
# https://www.geeksforgeeks.org/delete-n-nodes-after-m-nodes-of-a-linked-list/
from linkedlist import SinglyLinkedList


def delete_n_nodes_after_every_m_nodes(singly_linked_list: SinglyLinkedList):
    current_node = singly_linked_list.head

    while current_node:


