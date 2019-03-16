# Problem Statement
# https://www.geeksforgeeks.org/lru-cache-implementation/


from linkedlists import BuildDoublyLinkedList, DoublyLinkedList

MAX_CACHE_SIZE = 4


class LRUCache:
    def __init__(self, cache_size=MAX_CACHE_SIZE):
        self.deque = self.get_deque_instance()
        self.key_node_map = {}
        self.max_cache_size = cache_size
        self.len_of_deque = 0

    def get_new_node(self, node_data):
        return self.deque._get_new_node(node_data)

    def _remove_deque_node(self, node):
        self.deque.remove(node)

    def remove(self, node):
        del self.key_node_map[node.data]
        self._remove_deque_node(node)
        self.len_of_deque -= 1 if self.len_of_deque > 0 else 0

    def pop_right(self):
        tail_node = self.deque.tail
        self.remove(tail_node)
        return tail_node

    def append_left(self, new_deque_node):
        self.deque.insert_at_begin(node=new_deque_node)
        self.len_of_deque += 1

    def reset_node(self, node, new_data=None):
        if new_data:
            node.data = new_data
        node.previous = None
        node.next = None

    def get_attr(self, attr_key):
        deque_node = self.key_node_map.get(attr_key, None)
        if deque_node:
            self.remove(deque_node)
            self.reset_node(deque_node)
            self.append_left(deque_node)
        else:
            if self.is_deque_full:
                tail_node = self.pop_right()
                self.reset_node(tail_node, attr_key)
                self.append_left(tail_node)
                self.key_node_map[attr_key] = tail_node
            else:
                new_node = self.get_new_node(attr_key)
                self.append_left(new_node)
                self.key_node_map[attr_key] = new_node

    def print_cache(self):
        self.deque.print_linked_list()

    @classmethod
    def get_deque_instance(cls):
        return BuildDoublyLinkedList().get_ll()

    @property
    def is_deque_full(self):
        ###############
        # Method 1
        return self.len_of_deque == self.max_cache_size
        ###############
        # Method 2
        # return len(self.key_node_map) >= self.max_cache_size
        ###############


# driver code
def run():
    lru_cache = LRUCache()
    print('Cache state on various events: ')

    for num in range(1, 6):
        lru_cache.get_attr(num)
        lru_cache.print_cache()

    lru_cache.get_attr(2)
    lru_cache.print_cache()


if __name__ == '__main__':
    run()
