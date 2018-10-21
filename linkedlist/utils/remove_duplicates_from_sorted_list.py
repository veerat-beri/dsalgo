# Problem Statement
# https://www.geeksforgeeks.org/remove-duplicates-from-a-sorted-linked-list/


from linkedlist import SinglyLinkedListNode, SinglyLinkedList, BuildSinglyLinkedList


def remove_duplicates_from_sorted_list(sorted_linked_list: SinglyLinkedList):
    current_node = sorted_linked_list.head
    while current_node:
        next_node = current_node.next
        if next_node:
            if next_node.data == current_node.data:
                current_node.next = next_node.next
                continue
        current_node = next_node


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
    remove_duplicates_from_sorted_list(sorted_singly_singly_list)
    sorted_singly_singly_list.print_linked_list()


if __name__ == '__main__':
    run()
