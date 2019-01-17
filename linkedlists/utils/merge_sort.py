# Problem Statement
# https://www.geeksforgeeks.org/merge-sort-for-linked-list/


from linkedlists import SinglyLinkedListNode, BuildSinglyLinkedList, SinglyLinkedList


def merge_two_sorted_ll(linked_list_1: SinglyLinkedList, linked_list_2: SinglyLinkedList):
    current_node_of_ll_1 = linked_list_1.head
    current_node_of_ll_2 = linked_list_2.head

    while current_node_of_ll_1 and current_node_of_ll_2:
        if current_node_of_ll_1.data > current_node_of_ll_2.data:


            current_node_of_ll_2 = current_node_of_ll_2.next


def get_merge_sorted_ll(linked_list: SinglyLinkedList):
    def _get_merge_sorted_ll():
        pass


# driver code
def run():
    list_of_nodes = [SinglyLinkedListNode(12), SinglyLinkedListNode(11), SinglyLinkedListNode(13),
                     SinglyLinkedListNode(5), SinglyLinkedListNode(6), SinglyLinkedListNode(7)]
    singly_linked_list = BuildSinglyLinkedList(list_of_nodes=list_of_nodes).build()
    print('Linked List before sort: ')
    singly_linked_list.print_linked_list()

    print('Linked List after sort: ')
    singly_linked_list.print_linked_list()


if __name__ == '__main__':
    run()
