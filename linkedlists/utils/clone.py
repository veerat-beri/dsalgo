# Problem Statement
# https://www.geeksforgeeks.org/a-linked-list-with-next-and-arbit-pointer/


from collections import OrderedDict
from linkedlists import SinglyLinkedList
from linkedlists.build_linked_list import _BuildLinkedList


class BuildCustomLinkedList(_BuildLinkedList):
    def _get_ll_instance(self):
        return CustomLinkedList()


class CustomLinkedList(SinglyLinkedList):
    class CustomNode(SinglyLinkedList.SinglyLinkedListNode):
        def __init__(self, data, **kwargs):
            super().__init__(data, **kwargs)
            self.random = None

    def _get_new_node(self, node_data):
        return self.CustomNode(node_data)

    def print_linked_list(self, **kwargs):
        current_node = self.head
        while current_node:
            print(current_node.data, f'({id(current_node)})', f'({current_node.random.data})', sep='', end='  ')
            current_node = current_node.next


class CloneLinkedList:
    ############################################################
    # Space Complexity: O(N)
    def __init__(self, linked_list: CustomLinkedList):
        # https://mail.python.org/pipermail/python-dev/2017-December/151283.html
        # From python 3.7 onwards default dict is OrderedDict(),
        # but explicitly made OrderedDict to maintain backward compatibility of code

        # Format => {'old_node': 'new_node'}
        self.old_node_new_node_map = OrderedDict()

        self.linked_list = linked_list

    def __clone_data(self):
        current_node = self.linked_list.head
        while current_node:
            new_node = self.linked_list._get_new_node(current_node.data)
            self.old_node_new_node_map[current_node] = new_node
            current_node = current_node.next

    def __clone_ptrs(self):
        for (old_node, new_node) in self.old_node_new_node_map.items():
            new_node.next = self.old_node_new_node_map.get(old_node.next)
            new_node.random = self.old_node_new_node_map.get(old_node.random)

    def clone(self):
        self.__clone_data()
        self.__clone_ptrs()
        return CustomLinkedList(head=self.old_node_new_node_map[next(iter(self.old_node_new_node_map))])
    ############################################################
    # Space Complexity: O(1)
    # https://www.geeksforgeeks.org/clone-linked-list-next-random-pointer-o1-space/

    # def clone(self):
    #     pass
    ############################################################


# driver code
def run():
    print('Old Linked List: ')
    custom_linked_list = BuildCustomLinkedList(list_of_nodes=[1, 2, 3, 4, 5]).get_ll()
    n1 = custom_linked_list.head
    n2 = n1.next
    n3 = n2.next
    n4 = n3.next
    n5 = n4.next

    n1.random = n3
    n2.random = n1
    n3.random = n5
    n4.random = n3
    n5.random = n2

    custom_linked_list.print_linked_list()
    new_custom_linked_list = CloneLinkedList(custom_linked_list).clone()
    print('\nNew Cloned Linked List: ')
    new_custom_linked_list.print_linked_list()


if __name__ == '__main__':
    run()
