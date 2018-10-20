from linkedlist import BuildSinglyLinkedList, SinglyLinkedListNode


def recursively_print_linked_list(current_node: SinglyLinkedListNode):
    if current_node:
        print(current_node.data, end='  ')
        recursively_print_linked_list(current_node.next)


# driver code
def run():
    singly_linked_list = BuildSinglyLinkedList(auto_populate=True).build()
    recursively_print_linked_list(singly_linked_list.head)


if __name__ == '__main__':
    run()
