# Problem Statement
# https://www.geeksforgeeks.org/lru-cache-implementation/


from linkedlists import BuildDoublyLinkedList, DoublyLinkedList

MAX_CACHE_SIZE = 4


class LRUCache:
    def __init__(self, cache_size=MAX_CACHE_SIZE):
        self.deque = self.get_deque_instance()
        self.key_node_map = {}
        self.max_cache_size = cache_size

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

    def remove(self, node):
        del self.key_node_map[node.data]
        self._remove_deque_node(node)

    def pop_right(self):
        tail_node = self.deque.tail
        self.remove(tail_node)
        return tail_node

    def append_left(self, new_deque_node):
        new_deque_node.next = self.deque.head
        self.deque.head.previous = new_deque_node
        self.deque.head = new_deque_node
        new_deque_node.previous = None

    def get_attr(self, attr_key):
        deque_node = self.key_node_map.get(attr_key, None)
        if deque_node:
            self.remove(deque_node)
            self.append_left(deque_node)
        else:
            if self.is_deque_full:
                tail_node = self.pop_right()
                tail_node.data = attr_key
                self.append_left(tail_node)
                self.key_node_map[attr_key] = tail_node
            else:
                new_node = self.get_new_node(attr_key)
                self.append_left(new_node)
                self.key_node_map[attr_key] = new_node

    def print_cache(self):
        for key,  in

    @classmethod
    def get_deque_instance(cls):
        return BuildDoublyLinkedList().get_ll()

    @property
    def is_deque_full(self):
        # return self.len_of_linked_list == MAX_CACHE_SIZE
        return len(self.key_node_map) >= self.max_cache_size


# driver code
def run():
    lru_cache = LRUCache()
    for num in range(1, 6):
        lru_cache.get_attr(1)


if __name__ == '__main__':
    run()
