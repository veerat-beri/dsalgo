# Problem Statement
# https://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/
from linkedlist import SinglyLinkedList, BuildSinglyLinkedList


def point_of_intersection_of_two_lists(linked_list_1: SinglyLinkedList, linked_list_2: SinglyLinkedList):
    current_node_1 = linked_list_1.head
    current_node_2 = linked_list_2.head

    no_of_nodes_in_list_1 = 0
    no_of_nodes_in_list_2 = 0

    while current_node_1:
        no_of_nodes_in_list_1 += 1
        current_node_1 = current_node_1.next

    while current_node_2:
        no_of_nodes_in_list_2 += 1
        current_node_2 = current_node_2.next

    difference_in_count = no_of_nodes_in_list_1 - no_of_nodes_in_list_2

    start_point_of_one_list = None
    start_point_of_other_list = None

    if difference_in_count:
        linked_to_head_start = linked_list_2 if difference_in_count < 0 else linked_list_1
        current_node = linked_to_head_start.head

        for _ in range(difference_in_count):
            current_node = current_node.next

        start_point_of_one_list = (linked_to_head_start ^ (linked_list_1 ^ linked_list_2)).head
        start_point_of_other_list = current_node

    current_node_1 = start_point_of_one_list or linked_list_1.head
    current_node_2 = start_point_of_other_list or linked_list_2.head

    while current_node_1 and current_node_2:
        if current_node_1 == current_node_2:
            return current_node_1

        current_node_2 = current_node_2.next
        current_node_1 = current_node_1.next


# driver code
def run():
    list_nodes_of_list_1 = [

    ]
    list_nodes_of_list_2 =[

    ]
    singly_linked_list1 = BuildSinglyLinkedList(list_of_nodes=list_nodes_of_list_1).build()
    singly_linked_list2 = BuildSinglyLinkedList(list_of_nodes=list_nodes_of_list_2).build()
    point_of_intersection_of_two_lists(singly_linked_list1, singly_linked_list2)


if __name__ == '__main__':
    run()

