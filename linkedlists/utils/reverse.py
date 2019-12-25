# Problem Statement
# https://www.geeksforgeeks.org/reverse-a-linked-list/


from linkedlists import BuildSinglyLinkedList, SinglyLinkedList


######################################
# Iterative approach
######################################
def reverse_linked_list(linked_list: SinglyLinkedList):
    current_node = linked_list.head
    previous_node = None

    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node

    return previous_node


######################################
# Recursive Approach
######################################
def reverse_linked_list_recursive(linked_list: SinglyLinkedList):
    def reverse_linked_list(current_node: SinglyLinkedList.Node, previous_node: SinglyLinkedList.Node = None):
        if not current_node:
            return previous_node

        next_node = current_node.next
        current_node.next = previous_node
        return reverse_linked_list(next_node, current_node)

    return reverse_linked_list(linked_list.head)


######################################

# driver code
def run():
    singly_linked_list = BuildSinglyLinkedList(auto_populate=True).get_ll()

    print('Given Linked List: ')
    singly_linked_list.print_linked_list()

    print('\nLinked List after reversal: ')
    new_head = reverse_linked_list(singly_linked_list)
    singly_linked_list.head = new_head
    singly_linked_list.print_linked_list()


if __name__ == '__main__':
    run()
