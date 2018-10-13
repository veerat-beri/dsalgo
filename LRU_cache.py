from linked_list import DoublyLinkedList, Node, BuildDoublyLinkedList


linked_list_of_records = BuildDoublyLinkedList().build()

LINKED_LIST_SIZE = 4


class LRUCache(DoublyLinkedList):
    def __init__(self):
        self.key_node_map = {}

    def get_attr(self, key):
        return self.key_node_map

    def set_attr(self, key, value):
        pass