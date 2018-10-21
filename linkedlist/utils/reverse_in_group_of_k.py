# Problem Statement
# https://www.geeksforgeeks.org/reverse-a-list-in-groups-of-given-size/


from linkedlist import SinglyLinkedListNode, BuildSinglyLinkedList


def reverse_in_group_of_k(head: SinglyLinkedListNode, k):
    current_node = head
    previous_node = None

    count_k = k
    while current_node and count_k:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
        count_k -= 1

    if current_node:
        head.next = reverse_in_group_of_k(current_node, k)

    return previous_node


# driver code
def run():
    list_of_nodes = [
        SinglyLinkedListNode(60), SinglyLinkedListNode(70), SinglyLinkedListNode(80),
        SinglyLinkedListNode(90), SinglyLinkedListNode(100),
    ]
    singly_linked_list = BuildSinglyLinkedList(list_of_nodes=list_of_nodes, auto_populate=True).build()
    k = 3
    print('Given Linked List: ')
    singly_linked_list.print_linked_list()

    print('\n\nLinked List after reverse action: ')
    new_head = reverse_in_group_of_k(singly_linked_list.head, k)
    singly_linked_list.head = new_head
    singly_linked_list.print_linked_list()


if __name__ == '__main__':
    run()

