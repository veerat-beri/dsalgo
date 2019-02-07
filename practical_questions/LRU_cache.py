# Problem Statement
# https://www.geeksforgeeks.org/lru-cache-implementation/


from linkedlists import BuildDoublyLinkedList, DoublyLinkedList

MAX_CACHE_SIZE = 4

class LRUCache:
    def __init__(self):
        self.deque = self.get_deque_instance()
        self.key_node_map = {}

    def get_attr(self, key):
        return self.key_node_map[key]

    def get_new_node(self, node_data):
        return self.deque._get_new_node(node_data)

    def _remove_deque_node(self, node):
        if node.previous is None:  # node is head node
            self.deque.head = node.next
        else:
            node.previous.next = node.next

        if node.next is None:  # node is tail node
            self.deque.tail = node.previous
        else:
            node.next.previous = node.previous

    def remove(self, attr_key=None):
        deque_node = self.key_node_map[attr_key or self.deque.tail.data]
        del deque_node
        self._remove_deque_node(deque_node)

    def append_left(self, new_deque_node):
        new_deque_node.next = self.deque.head
        self.deque.head.previous = new_deque_node
        self.deque.head = new_deque_node

    def set_attr(self, attr_key, attr_value):
        ll_node = self.key_node_map.get(attr_key, None)
        if ll_node:
            self.remove(attr_key)
            self.append_left(ll_node)
        else:
            if self.is_deque_full:
                self.remove()
                self.append_left(self.get_new_node(attr_value))
            else:


    def get_deque_instance(self):
        return BuildDoublyLinkedList().get_ll()

    @property
    def is_deque_full(self):
        # return self.len_of_linked_list == MAX_CACHE_SIZE
        return len(self.key_node_map) >= MAX_CACHE_SIZE


# driver code
def run():
    pass


if __name__ == '__main__':
    run()