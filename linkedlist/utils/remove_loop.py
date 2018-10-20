# Problem Statement
# https://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/


from linkedlist.utils import check_loop_exists
from linkedlist import BuildSinglyLinkedList, SinglyLinkedListNode, SinglyLinkedList


def remove_loop(singly_linked_list: SinglyLinkedList, node_in_loop: SinglyLinkedListNode):
    slow_ptr = singly_linked_list.head
    fast_ptr = node_in_loop

    while fast_ptr.next != slow_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next

    fast_ptr.next = None


# driver code
def run():
    pass



