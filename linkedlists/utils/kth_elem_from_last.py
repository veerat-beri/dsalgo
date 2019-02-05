# Problem Statement
# https://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/


from linkedlists import SinglyLinkedList, BuildSinglyLinkedList


def find_kth_node_from_end(singly_linked_list: SinglyLinkedList, k):
    assert len(singly_linked_list) >= k, f'\n\n{k} is greater than len of list'
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
    singly_linked_list = BuildSinglyLinkedList(auto_populate=True).get_ll()
    k = 3

    print('Given Linked List: ')
    singly_linked_list.print_linked_list()

    required_node = find_kth_node_from_end(singly_linked_list, k)
    print(f'\n{k}th node from end: ', required_node.data)


if __name__ == '__main__':
    run()
