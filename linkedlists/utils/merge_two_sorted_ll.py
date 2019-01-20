# Problem Statement
# https://www.geeksforgeeks.org/merge-two-sorted-linked-lists/


from linkedlists import BuildSinglyLinkedList, SinglyLinkedList


def get_sorted_merged_ll(linked_list_1: SinglyLinkedList, linked_list_2: SinglyLinkedList):
        current_node_of_ll_1 = linked_list_1.head
        current_node_of_ll_2 = linked_list_2.head
        new_ll = SinglyLinkedList()

        while current_node_of_ll_1 and current_node_of_ll_2:
            if current_node_of_ll_1.data > current_node_of_ll_2.data:
                while current_node_of_ll_2 and current_node_of_ll_2.data < current_node_of_ll_1.data:
                    temp_node_holder = current_node_of_ll_2.next
                    current_node_of_ll_2.next = current_node_of_ll_1
                    current_node_of_ll_2 = temp_node_holder

