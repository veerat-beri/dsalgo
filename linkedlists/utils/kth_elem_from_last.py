from linkedlists import SinglyLinkedList, BuildSinglyLinkedList


class KthElemFromEnd:
    @staticmethod
    def __validate_input(singly_linked_list, k):
        assert len(singly_linked_list) >= k, f'\n\n{k} is greater than len of list'

    def __init__(self, singly_linked_list: SinglyLinkedList, k):
        self.singly_linked_list = singly_linked_list
        self.k = k
        self.__validate_input(singly_linked_list, k)

    ###########################################################################
    # Problem Statement
    # https://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/
    def find(self):
        slow_ptr = self.singly_linked_list.head
        fast_ptr = self.singly_linked_list.head

        for _ in range(self.k):
            # Not required as we already validated the input
            # if not fast_ptr:
            #     return
            fast_ptr = fast_ptr.next

        while fast_ptr:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next

        return slow_ptr

    ###########################################################################
    # Problem Statement
    # https://leetcode.com/problems/remove-nth-node-from-end-of-list/
    def remove(self):
        slow_ptr = self.singly_linked_list.head
        fast_ptr = self.singly_linked_list.head
        previous_slow_ptr = None

        for _ in range(self.k):
            fast_ptr = fast_ptr.next

        while fast_ptr:
            previous_slow_ptr = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next

        deleted_node_next = slow_ptr.next

        # middle/end node need to be removed
        if previous_slow_ptr:
            previous_slow_ptr.next = deleted_node_next
        # head node needs to be removed
        else:
            self.singly_linked_list.head = deleted_node_next

        del slow_ptr
    ###########################################################################

# driver code
def run():
    singly_linked_list = BuildSinglyLinkedList(auto_populate=True).get_ll()
    k = 3

    print('Given Linked List: ')
    singly_linked_list.print_linked_list()

    required_node = KthElemFromEnd(singly_linked_list, k).find()
    print(f'\n{k}th node from end: ', required_node.data)

    print(f'\nRemoving {k}th node from end: ', required_node.data)
    KthElemFromEnd(singly_linked_list, k).remove()
    print(f'\nLinked List after removing kth node: ')
    singly_linked_list.print_linked_list()


if __name__ == '__main__':
    run()
