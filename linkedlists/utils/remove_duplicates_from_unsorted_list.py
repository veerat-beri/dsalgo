# Problem Statement
# https://www.geeksforgeeks.org/remove-duplicates-from-an-unsorted-linked-list/

from linkedlists import SinglyLinkedList, BuildSinglyLinkedList


def remove_duplicates_from_unsorted_list(linked_list: SinglyLinkedList):
    """
    Function to remove duplicates from a unsorted linked list
    :param linked_list: Linked list from which duplicates is to be removed.
    :return: None
    """
    # Set to store seen values
    unique_list_nodes = set()
    current_node = linked_list.head

    if current_node:
        unique_list_nodes.add(current_node.data)
        previous_node = current_node
        current_node = current_node.next

        while current_node:
            # If current value is seen before
            if current_node.data in unique_list_nodes:
                previous_node.next = current_node.next
            else:
                previous_node = current_node
                unique_list_nodes.add(current_node.data)
            current_node = current_node.next


# driver code
def run():
    unsorted_singly_singly_list = BuildSinglyLinkedList(list_of_nodes=[10, 50, 30, 20, 10], auto_populate=True).get_ll()

    print('Given Lined List: ')
    unsorted_singly_singly_list.print_linked_list()

    print('\n\nLinked List after duplicate removal: ')
    remove_duplicates_from_unsorted_list(unsorted_singly_singly_list)
    unsorted_singly_singly_list.print_linked_list()


if __name__ == '__main__':
    run()

