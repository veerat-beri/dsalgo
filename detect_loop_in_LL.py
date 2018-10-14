from linked_list import SinglyLinkedListNode, SinglyLinkedList, BuildSinglyLinkedList


def detect_loop(singly_linked_list: SinglyLinkedList):
    current_node = singly_linked_list.head

    while current_node:
        next_node = current_node.next
        if not next_node:
            return False
        next_to_next_node = next_node.next

        if not next_to_next_node:
            return False

        if current_node == next_to_next_node:
            return True

        current_node = current_node.next


# driver code
def run():
    n1 = SinglyLinkedListNode(10)
    n2 = SinglyLinkedListNode(20)
    n1.next = n2
    n3 = SinglyLinkedListNode(30)
    n2.next = n3
    n4 = SinglyLinkedListNode(40)
    n3.next = n4
    n5 = SinglyLinkedListNode(50)
    n5.next = n3

    singly_linked_list = SinglyLinkedList(head=n1)

    is_loop_present = detect_loop(singly_linked_list)
    if is_loop_present:
        print('Yes loop exists')
    else:
        print('No loop does not exists')

