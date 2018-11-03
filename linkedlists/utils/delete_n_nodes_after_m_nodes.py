# Problem Statement
# https://www.geeksforgeeks.org/delete-n-nodes-after-m-nodes-of-a-linked-list/


from linkedlists import SinglyLinkedList, BuildSinglyLinkedList, SinglyLinkedListNode


def delete_n_nodes_after_every_m_nodes(singly_linked_list: SinglyLinkedList, m, n):
    current_node = singly_linked_list.head

    while current_node:
        count_m = m - 1  # -1 as 1st element is already counted as current elem
        count_n = n

        while current_node and count_m >= 1:
            count_m -= 1
            current_node = current_node.next

        if not current_node:
            return

        node_to_be_deleted = current_node.next
        while node_to_be_deleted and count_n >= 1:
            count_n -= 1
            node_to_be_deleted = node_to_be_deleted.next

        current_node.next = node_to_be_deleted
        current_node = current_node.next


# driver code
def run():
    list_of_nodes = [
        SinglyLinkedListNode(60), SinglyLinkedListNode(70), SinglyLinkedListNode(80),
        SinglyLinkedListNode(90), SinglyLinkedListNode(100), SinglyLinkedListNode(110),
        SinglyLinkedListNode(120), SinglyLinkedListNode(130),
    ]

    singly_linked_list = BuildSinglyLinkedList(list_of_nodes=list_of_nodes, auto_populate=True).build()
    m = 2
    n = 2

    print('Given Linked List:')
    singly_linked_list.print_linked_list()

    delete_n_nodes_after_every_m_nodes(singly_linked_list, m, n)

    print('\n\nLinked List after deletion: ')
    singly_linked_list.print_linked_list()


if __name__ == '__main__':
    run()








