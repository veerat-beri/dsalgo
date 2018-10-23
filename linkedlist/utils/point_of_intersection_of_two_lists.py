# Problem Statement
# https://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/


from linkedlist import SinglyLinkedList, BuildSinglyLinkedList, SinglyLinkedListNode


# Based on Method 3 (Using difference of node counts)
def point_of_intersection_of_two_lists(singly_linked_list_1: SinglyLinkedList, singly_linked_list_2: SinglyLinkedList):

    # This functionality already built-in base linked_list class

    # def calc_no_node_in_list(singly_linked_list: SinglyLinkedList):
    #     no_of_nodes_in_list = 0
    #     current_node = singly_linked_list.head
    #     while current_node:
    #         no_of_nodes_in_list += 1
    #         current_node = current_node.next
    #
    #     return no_of_nodes_in_list

    def get_right_start_nodes_in_each_list(no_of_nodes_in_list_1, no_of_nodes_in_list_2):
        difference_in_count = no_of_nodes_in_list_1 - no_of_nodes_in_list_2

        node_in_one_list = singly_linked_list_1.head
        node_in_other_list = singly_linked_list_2.head

        if difference_in_count < 0:
            current_node = singly_linked_list_2.head
            for _ in range(abs(difference_in_count)):
                current_node = current_node.next

            node_in_other_list = current_node

        elif difference_in_count > 0:
            current_node = singly_linked_list_1.head
            for _ in range(abs(difference_in_count)):
                current_node = current_node.next

            node_in_one_list = current_node

        return node_in_one_list, node_in_other_list

    no_of_nodes_in_list_1 = len(singly_linked_list_1)  # calc_no_node_in_list(singly_linked_list_1)
    no_of_nodes_in_list_2 = len(singly_linked_list_2)  # calc_no_node_in_list(singly_linked_list_2)

    node_in_one_list, node_in_other_list = get_right_start_nodes_in_each_list(
        no_of_nodes_in_list_1, no_of_nodes_in_list_2
    )

    while node_in_one_list and node_in_other_list:
        if node_in_one_list == node_in_other_list:
            return node_in_one_list

        node_in_one_list = node_in_one_list.next
        node_in_other_list = node_in_other_list.next

    return None


# driver code
def run():
    list_nodes_of_list_1 = [
        SinglyLinkedListNode(60), SinglyLinkedListNode(70), SinglyLinkedListNode(80),
        SinglyLinkedListNode(90),
    ]

    singly_linked_list1 = BuildSinglyLinkedList(list_of_nodes=list_nodes_of_list_1, auto_populate=True).build()
    singly_linked_list2 = BuildSinglyLinkedList(list_of_nodes=[SinglyLinkedListNode(5)] + list_nodes_of_list_1).build()
    intersection_node = point_of_intersection_of_two_lists(singly_linked_list1, singly_linked_list2)

    print('Given Linked List 1: ')
    singly_linked_list1.print_linked_list(with_address=True)

    print('\n\nGiven Linked List 2: ')
    singly_linked_list2.print_linked_list(with_address=True)

    if intersection_node:
        print('\n\nIntersection Node: ', intersection_node.data, f'({id(intersection_node)})', sep='')
    else:
        print('\n\nNo Intersection Node exists')


if __name__ == '__main__':
    run()

