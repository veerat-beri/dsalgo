# Problem Statement
# https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/


from linkedlists import SinglyLinkedList
from linkedlists.build_linked_list import BuildSinglyLinkedListWithLoop


# Using Floyd’s Cycle-Finding Algorithm
def check_loop_exists(singly_linked_list: SinglyLinkedList):
    slow_ptr = singly_linked_list.head
    fast_ptr = singly_linked_list.head

    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

        if slow_ptr == fast_ptr:
            return True, slow_ptr
    return False, None


# driver code
def run():
    #####################################
    # One Way to make linked list with loop

    # n1 = SinglyLinkedListNode(10)
    # n2 = SinglyLinkedListNode(20)
    # n1.next = n2
    # n3 = SinglyLinkedListNode(30)
    # n2.next = n3
    # n4 = SinglyLinkedListNode(40)
    # n3.next = n4
    # n5 = SinglyLinkedListNode(50)
    # n4.next = n5
    # n5.next = n3
    #
    # singly_linked_list = SinglyLinkedList(head=n1)

    ######################################
    # Other Way

    singly_linked_list = BuildSinglyLinkedListWithLoop(auto_populate=True).build()
    ######################################
    is_loop_present = check_loop_exists(singly_linked_list)

    if is_loop_present:
        print('Yes loop exists')
    else:
        print('No loop does not exists')


if __name__ == '__main__':
    run()
