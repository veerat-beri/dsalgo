from linkedlists import BuildSinglyLinkedList, SinglyLinkedList


def recursively_print_linked_list(singly_ll: SinglyLinkedList):
    def _recursively_print_linked_list(current_node: SinglyLinkedList.SinglyLinkedListNode):
        if current_node:
            print(current_node.data, end='  ')
            _recursively_print_linked_list(current_node.next)
    _recursively_print_linked_list(singly_ll.head)


# driver code
def run():
    singly_linked_list = BuildSinglyLinkedList(auto_populate=True).get_ll()
    recursively_print_linked_list(singly_linked_list)


if __name__ == '__main__':
    run()
