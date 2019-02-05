# Problem Statement
# https://www.geeksforgeeks.org/lru-cache-implementation/


from linkedlists import BuildDoublyLinkedList, DoublyLinkedList

MAX_CACHE_SIZE = 4


class LRUCache:
    def __init__(self, list_of_nodes: []=None):
        self.doubly_ended_queue = self.get_ll_instance(list_of_nodes)
        self.key_node_map = {}

    def get_attr(self, key):
        return self.key_node_map

    def get_new_node(self, node_data):
        return

    def set_attr(self, attr_key, attr_value):
        ll_node = self.key_node_map.get(attr_key, None)
        if ll_node:
            self.remove(ll_node)
            self.append_left(ll_node)
        else:
            if len(self.key_node_map) >= MAX_CACHE_SIZE:
                self.remove()
                self.append_left(self.get_new_node(attr_value))

    def get_ll_instance(self, list_of_nodes):
        return BuildDoublyLinkedList(list_of_nodes=list_of_nodes, insert_at_end=False).get_ll()

    @property
    def is_linked_list_full(self):
        return self.len_of_linked_list == MAX_LINKED_LIST_SIZE


# driver code
def run():
    pass


if __name__ == '__main__':
    run()