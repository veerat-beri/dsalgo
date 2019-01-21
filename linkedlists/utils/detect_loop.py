# Problem Statement
# https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/


from linkedlists import SinglyLinkedList, BuildSinglyLinkedListWithLoop


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
    singly_linked_list = BuildSinglyLinkedListWithLoop(auto_populate=True).get_ll()
    is_loop_present = check_loop_exists(singly_linked_list)

    if is_loop_present:
        print('Yes loop exists')
    else:
        print('No loop does not exists')


if __name__ == '__main__':
    run()
