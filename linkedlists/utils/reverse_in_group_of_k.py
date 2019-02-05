# Problem Statement
# https://www.geeksforgeeks.org/reverse-a-list-in-groups-of-given-size/


from linkedlists import SinglyLinkedList, BuildSinglyLinkedList


def reverse_in_group_of_k(singly_ll: SinglyLinkedList, k):
    def _reverse_in_group_of_k(head):
        current_node = head
        previous_node = None

        count_k = k
        while current_node and count_k:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            count_k -= 1

        if current_node:
            head.next = _reverse_in_group_of_k(current_node)

        return previous_node  # returns new head of the reversed LL
    return _reverse_in_group_of_k(singly_ll.head)


# driver code
def run():
    singly_linked_list = BuildSinglyLinkedList(list_of_nodes=[60, 70, 80, 90, 100, ], auto_populate=True).get_ll()
    k = 3
    print('Given Linked List: ')
    singly_linked_list.print_linked_list()

    print('\nLinked List after reverse action: ')
    new_head = reverse_in_group_of_k(singly_linked_list, k)
    singly_linked_list.head = new_head
    singly_linked_list.print_linked_list()


if __name__ == '__main__':
    run()

