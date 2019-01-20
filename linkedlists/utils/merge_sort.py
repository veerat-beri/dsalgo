# Problem Statement
# https://www.geeksforgeeks.org/merge-sort-for-linked-list/


from linkedlists import BuildSinglyLinkedList, SinglyLinkedList


def get_merge_sorted_ll(linked_list: SinglyLinkedList):
    def _get_merge_sorted_ll():
        pass


# driver code
def run():
    list_of_nodes = [12, 11, 13, 5, 6, 7, ]
    singly_linked_list = BuildSinglyLinkedList(list_of_nodes=list_of_nodes).get_ll()
    print('Linked List before sort: ')
    singly_linked_list.print_linked_list()

    print('\nLinked List after sort: ')
    singly_linked_list.print_linked_list()


if __name__ == '__main__':
    run()
