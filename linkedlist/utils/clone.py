# Problem Statement
# https://www.geeksforgeeks.org/a-linked-list-with-next-and-arbit-pointer/


from collections import OrderedDict
from linkedlist import SinglyLinkedList, SinglyLinkedListNode
from linkedlist.build_linked_list import _BuildLinkedList


class BuildCustomLinkedList(_BuildLinkedList):
    def __init__(self, **kwargs):
        super(BuildCustomLinkedList, self).__init__(**kwargs)

    def _create_linked_list(self):
        if not self._linked_list:
            self._linked_list = CustomLinkedList()

    def _create_list_of_nodes(self):
        pass


class CustomLinkedList(SinglyLinkedList):
    def __init__(self, head: 'CustomNode'=None, **kwargs):
        super(CustomLinkedList, self).__init__(head, **kwargs)

    def print_linked_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, f'({current_node.random.data})', sep='', end='  ')
            current_node = current_node.next


class CustomNode(SinglyLinkedListNode):
    def __init__(self, data, **kwargs):
        super(CustomNode, self).__init__(data, **kwargs)
        self.random = None


class CloneLinkedList:
    def __init__(self, linked_list: CustomLinkedList):
        # https://mail.python.org/pipermail/python-dev/2017-December/151283.html
        # From python 3.7 onwards default dict is OrderedDict(),
        # but explicitly made OrderedDict to maintain backward compatibility of code

        # Format => {'old_node': 'new_node'}
        self.old_node_new_node_map = OrderedDict()

        self._linked_list = linked_list
        self.new_linked_list = CustomLinkedList()

    def __clone_data(self):
        current_node = self._linked_list.head

        while current_node:
            new_node = CustomNode(current_node.data)
            self.old_node_new_node_map[current_node] = new_node

    def __clone_ptrs(self):
        for (old_node, new_node) in self.old_node_new_node_map.items():
            print(old_node.data, new_node.data)
            new_node.next = self.old_node_new_node_map[old_node.next]
            new_node.random = self.old_node_new_node_map[old_node.random]

    def clone(self):
        self.__clone_data()
        self.__clone_ptrs()
        self.new_linked_list = next(iter(self.old_node_new_node_map))
        return self.new_linked_list


# driver code
def run():
    n1 = CustomNode(1)
    n2 = CustomNode(2)
    n3 = CustomNode(3)
    n4 = CustomNode(4)
    n5 = CustomNode(5)

    custom_linked_list = BuildCustomLinkedList(list_of_nodes=[n1, n2, n3, n4, n5]).build()
    n1.random = n3
    n2.random = n1
    n3.random = n5
    n4.random = n3
    n5.random = n2

    # custom_linked_list.print_linked_list()
    new_custom_linked_list = CloneLinkedList(custom_linked_list).clone()
    print('New Cloned Linked List: ')
    # new_custom_linked_list.print_linked_list()


if __name__ == '__main__':
    run()
