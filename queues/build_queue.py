from queues.queue import LinkedQueue


class _BuildQueue:
    def __init__(self, list_of_nodes=None, auto_populate=False, **kwargs):
        self.auto_populate = auto_populate
        self.list_of_nodes = self._get_list_of_nodes(list_of_nodes, auto_populate)
        self._queue = self._get_queue_instance()

    def _get_list_of_nodes(self, list_of_nodes, auto_populate):
        if list_of_nodes is None:
            list_of_nodes = []
        return ([10, 20, 30, 40, 50, ] if auto_populate else []) + list_of_nodes


class BuildLinkedQueue(_BuildQueue):
    def _get_queue_instance(self):
        return LinkedQueue()

    def build(self):
        for node in self.list_of_nodes:
            self._queue.push(node)

        return self._queue
