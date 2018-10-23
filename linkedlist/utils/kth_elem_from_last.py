# Problem Statement
# https://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/


from linkedlist import SinglyLinkedList, BuildSinglyLinkedList


def find_kth_node_from_end(singly_linked_list: SinglyLinkedList, k):
    slow_ptr = singly_linked_list.head
    fast_ptr = singly_linked_list.head

    for _ in range(k):
        if not fast_ptr:
            return
        fast_ptr = fast_ptr.next

    while fast_ptr:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next

    return slow_ptr


# driver code
def run():
    singly_linked_list = BuildSinglyLinkedList(auto_populate=True).build()
    k = 3

    print('Given Linked List: ')
    singly_linked_list.print_linked_list()

    required_node = find_kth_node_from_end(singly_linked_list, k)
    if required_node:
        print('\n\nKth node from end: ', required_node.data)
    else:
        print(f'\n\n{k} is greater than len of list')


if __name__ == '__main__':
    run()
