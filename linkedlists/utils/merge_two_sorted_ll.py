# Problem Statement
# https://www.geeksforgeeks.org/merge-two-sorted-linked-lists/


from linkedlists import BuildSinglyLinkedList, SinglyLinkedList


def get_sorted_merged_ll(linked_list_1: SinglyLinkedList, linked_list_2: SinglyLinkedList):
        current_node_of_ll_1 = linked_list_1.head
        current_node_of_ll_2 = linked_list_2.head
        new_ll = SinglyLinkedList()
        new_ll.head = SinglyLinkedList.SinglyLinkedListNode(None)
        current_node_of_new_ll = new_ll.head

        while current_node_of_ll_1 and current_node_of_ll_2:
            if current_node_of_ll_1.data > current_node_of_ll_2.data:
                current_node_of_new_ll.next = current_node_of_ll_2
                current_node_of_ll_2 = current_node_of_ll_2.next
            else:
                current_node_of_new_ll.next = current_node_of_ll_1
                current_node_of_ll_1 = current_node_of_ll_1.next
            current_node_of_new_ll = current_node_of_new_ll.next

        current_node_of_new_ll.next = None

        ###############
        # Insert remaining nodes, in case given two linked lists are of unequal length.
        while current_node_of_ll_2:
            current_node_of_new_ll.next = current_node_of_ll_2
            current_node_of_ll_2 = current_node_of_ll_2.next
            current_node_of_new_ll = current_node_of_new_ll.next

        while current_node_of_ll_1:
            current_node_of_new_ll.next = current_node_of_ll_1
            current_node_of_ll_1 = current_node_of_ll_1.next
            current_node_of_new_ll = current_node_of_new_ll.next
        ###############

        return new_ll.head.next  # return head of new sorted and merged list


# driver code
def run():
    singly_ll_1 = BuildSinglyLinkedList(list_of_nodes=[10, 30, 50, 80, 90]).get_ll()
    singly_ll_2 = BuildSinglyLinkedList(list_of_nodes=[20, 40, 50, 70]).get_ll()

    print('Sorted Linked list-1: ')
    singly_ll_1.print_linked_list()

    print('\nSorted Linked list-2: ')
    singly_ll_2.print_linked_list()

    new_sorted_mergd_ll = SinglyLinkedList(head=get_sorted_merged_ll(singly_ll_1, singly_ll_2))

    print('\nNew sorted Linked list after merge: ')
    new_sorted_mergd_ll.print_linked_list()


if __name__ == '__main__':
    run()