# Problem Statement
# https://www.geeksforgeeks.org/remove-duplicates-from-an-unsorted-linked-list/
from linkedlists import SinglyLinkedList, BuildSinglyLinkedList, SinglyLinkedListNode


def remove_duplicates_from_unsorted_list(linked_list: SinglyLinkedList):
    pass


# driver code
def run():
    list_of_nodes = [
        SinglyLinkedListNode(10), SinglyLinkedListNode(10), SinglyLinkedListNode(20),
        SinglyLinkedListNode(30), SinglyLinkedListNode(30), SinglyLinkedListNode(30)
    ]
    sorted_singly_singly_list = BuildSinglyLinkedList(list_of_nodes=list_of_nodes).build()

    print('Given Lined List: ')
    sorted_singly_singly_list.print_linked_list()

    print('\n\nLinked List after duplicate removal: ')
    remove_duplicates_from_unsorted_list(sorted_singly_singly_list)
    sorted_singly_singly_list.print_linked_list()


if __name__ == '__main__':
    run()

