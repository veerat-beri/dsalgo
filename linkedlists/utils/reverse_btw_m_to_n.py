# Problem Statement
# https://leetcode.com/problems/reverse-linked-list-ii/
# https://www.geeksforgeeks.org/reverse-sublist-linked-list/

from linkedlists import SinglyLinkedList, BuildSinglyLinkedList


def reverse_from_m_to_n(head: SinglyLinkedList.Node, m: int, n: int) -> SinglyLinkedList.Node:
    if m == n:
        return head

    current_node = head
    reverse_ll_elem_count = n - m + 1
    node_before_mth_node = None
    previous_node = None

    for _ in range(1, m):
        node_before_mth_node = current_node
        current_node = current_node.next

    mth_node = current_node

    while reverse_ll_elem_count:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
        reverse_ll_elem_count -= 1

    mth_node.next = current_node

    if node_before_mth_node:
        node_before_mth_node.next = previous_node
        return head

    return previous_node


# driver code
def run():
    singly_ll = BuildSinglyLinkedList(auto_populate=True).get_ll()
    m = 1
    n = 5

    print('Linked list before reversal: ')
    singly_ll.print_linked_list()

    print(f'Linked list after reversal from {m} to {n}: ')
    new_head = reverse_from_m_to_n(singly_ll.head, m, n)
    singly_ll = SinglyLinkedList(head=new_head)
    singly_ll.print_linked_list()


if __name__ == '__main__':
    run()
