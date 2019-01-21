# Problem Statement
# https://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/


from linkedlists import SinglyLinkedList, BuildSinglyLinkedListWithLoop
from linkedlists.utils import check_loop_exists


def remove_loop(singly_linked_list: SinglyLinkedList, node_in_loop: SinglyLinkedList.SinglyLinkedListNode):
    slow_ptr = singly_linked_list.head
    fast_ptr = node_in_loop

    while fast_ptr.next != slow_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next

    fast_ptr.next = None


# driver code
def run():
    singly_linked_list = BuildSinglyLinkedListWithLoop(auto_populate=True).get_ll()
    do_loop_exists, slow_ptr = check_loop_exists(singly_linked_list)

    if do_loop_exists:
        print('Yes Loop Exists in Linked List')
        remove_loop(singly_linked_list, slow_ptr)
        print('Linked List after loop removal: ', end='')
    else:
        print('No Loop exists.\nLinked List: ', end='')
    singly_linked_list.print_linked_list()


if __name__ == '__main__':
    run()






