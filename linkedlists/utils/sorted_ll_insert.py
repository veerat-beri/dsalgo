# Problem Statement
# https://www.geeksforgeeks.org/given-a-linked-list-which-is-sorted-how-will-you-insert-in-sorted-way/

from linkedlists import SinglyLinkedList, BuildSinglyLinkedList


# Time Complexity: O(N)
# Space Complexity: O(1)
def insert_in_sorted_ll(singly_linked_list: SinglyLinkedList, new_node_data: int):
    new_node = singly_linked_list.get_new_node(new_node_data)
    current_node = singly_linked_list.head

    # LL is empty
    if not current_node:
        singly_linked_list.head = new_node

    ############################################################
    # Code handling Method 1
    ############################################################
    # Head is larger than current node
    elif current_node.data > new_node_data:
        new_node.next = singly_linked_list.head
        singly_linked_list.head = new_node

    # Insert at required place after head
    else:
        while current_node.next and current_node.next.data < new_node_data:
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node
    ############################################################
    # Code handling Method 2
    ############################################################
    # else:
    #     previous_node = None
    #     while current_node and current_node.data < new_node_data:
    #         previous_node = current_node
    #         current_node = current_node.next
    #
    #     new_node.next = current_node
    #
    #     if previous_node:
    #         previous_node.next = new_node
    #     # Head is larger than current node
    #     else:
    #         singly_linked_list.head = new_node
    ############################################################


# driver code
def run():
    nodes_list = [10, 20, 30, 40, 50, ]
    new_node_data = 15
    singly_ll = BuildSinglyLinkedList(list_of_nodes=nodes_list).get_ll()

    print(f'Linked list before insert: ')
    singly_ll.print_linked_list()

    insert_in_sorted_ll(singly_ll, new_node_data)

    print(f'Linked list after inserting {new_node_data}: ')
    singly_ll.print_linked_list()


if __name__ == '__main__':
    run()
