from linked_list import DoublyLinkedList, Node


def find_mid_of_linked_list(linked_list: DoublyLinkedList):
    slow_ptr = linked_list.head
    fast_ptr = linked_list.head

    while slow_ptr.next and fast_ptr.next:
        # if slow_ptr.next:
        slow_ptr = slow_ptr.next

        # fast_ptr_half_way = fast_ptr.next
        # if fast_ptr_half_way:
        if fast_ptr.next.next:
            fast_ptr = fast_ptr.next.next
        else:
            return slow_ptr


linked_list = DoublyLinkedList()
nodes = [Node(1), Node(10), Node(20), Node(40), Node(50), Node(60)]
for node in nodes:
    linked_list.insert_at_begin(node)

mid_node = find_mid_of_linked_list(linked_list)
print(mid_node.data)
