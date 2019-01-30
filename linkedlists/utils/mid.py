# Problem Statement
# https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/


from linkedlists import BuildSinglyLinkedList, SinglyLinkedList


def find_mid_of_linked_list(linked_list: SinglyLinkedList=None, head=None, use_head=False):
    slow_ptr = head if use_head else linked_list.head
    fast_ptr = head if use_head else linked_list.head

    assert (head and use_head) or linked_list, 'Linked list or head is not provided'

    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return slow_ptr


# driver code
def run():
    singly_linked_list = BuildSinglyLinkedList(list_of_nodes=[60, ], auto_populate=True).get_ll()
    mid_node = find_mid_of_linked_list(singly_linked_list)
    print('Linked List: ', end='')
    singly_linked_list.print_linked_list()
    print('Mid is: ', end='')
    if mid_node:
        print(mid_node.data)
    else:
        print(mid_node)


if __name__ == '__main__':
    run()

