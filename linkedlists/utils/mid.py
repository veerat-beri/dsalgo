# Problem Statement
# https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/


from linkedlists import SinglyLinkedListNode, BuildSinglyLinkedList, SinglyLinkedList


def find_mid_of_linked_list(linked_list: SinglyLinkedList):
    slow_ptr = linked_list.head
    fast_ptr = linked_list.head

    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return slow_ptr


# driver code
def run():
    list_of_nodes = [SinglyLinkedListNode(1), SinglyLinkedListNode(10), SinglyLinkedListNode(20), SinglyLinkedListNode(40), SinglyLinkedListNode(50), SinglyLinkedListNode(60)]
    singly_linked_list = BuildSinglyLinkedList(list_of_nodes=list_of_nodes).build()
    mid_node = find_mid_of_linked_list(singly_linked_list)

    print('Linked List: ', end='')
    singly_linked_list.print_linked_list()
    print('\nMid is: ', end='')
    if mid_node:
        print(mid_node.data)
    else:
        print(mid_node)


if __name__ == '__main__':
    run()

