# Problem Statement
# https://www.geeksforgeeks.org/lru-cache-implementation/


from linkedlists import BuildDoublyLinkedList, DoublyLinkedList
#
MAX_LINKED_LIST_SIZE = 4  # cache size


class LRUCache:
    def __init__(self, singly_linked_list_of_records=None, list_of_nodes: [SinglyLinkedListNode]=None):
        self.singly_linked_list_of_records = BuildSinglyLinkedList(singly_linked_list_of_records, list_of_nodes).build()
        self.key_node_map = {}
        self.len_of_linked_list = 0

    def get_attr(self, key):
        return self.key_node_map

    def set_attr(self, key, value):
        # if not self.is_linked_list_full:
        #     self.
        pass

    @property
    def is_linked_list_full(self):
        return self.len_of_linked_list == MAX_LINKED_LIST_SIZE


# driver code
def run():
    pass


if __name__ == '__main__':
    run()