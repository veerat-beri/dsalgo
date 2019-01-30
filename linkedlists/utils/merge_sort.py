# Problem Statement
# https://www.geeksforgeeks.org/merge-sort-for-linked-list/


from linkedlists import BuildSinglyLinkedList, SinglyLinkedList
from linkedlists.utils import get_sorted_merged_ll


def find_mid_of_linked_list(head):
    slow_ptr = head
    fast_ptr = None
    if slow_ptr:
        fast_ptr = slow_ptr.next.next

    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return slow_ptr


def get_merge_sorted_ll(linked_list: SinglyLinkedList):
    def _get_merge_sorted_ll(head):
        if head.next is None:
            return head

        mid_node = find_mid_of_linked_list(head=head)
        next_ll_head = mid_node.next
        mid_node.next = None

        return get_sorted_merged_ll(head_1=_get_merge_sorted_ll(head), head_2=_get_merge_sorted_ll(next_ll_head), use_heads=True)

    if linked_list.head:
        return _get_merge_sorted_ll(linked_list.head)


# driver code
def run():
    list_of_nodes = [12, 11, 13, 5, 6, 7, ]
    singly_linked_list = BuildSinglyLinkedList(list_of_nodes=list_of_nodes).get_ll()
    print('Linked List before sort: ')
    singly_linked_list.print_linked_list()

    new_head = get_merge_sorted_ll(singly_linked_list)
    sorted_ll = SinglyLinkedList(head=new_head)
    print('Linked List after sort: ')
    sorted_ll.print_linked_list()


if __name__ == '__main__':
    run()
