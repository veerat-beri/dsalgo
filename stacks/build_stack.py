from stacks.stack import LinkedStack


class _BuildStack:
    def __init__(self, list_of_nodes=list(), auto_populate=False, **kwargs):
        self.auto_populate = auto_populate
        self.list_of_nodes = list_of_nodes
        self._stack = None

        self._create_stack()
        self._create_list_of_nodes()

    def _create_list_of_nodes(self):
        self.list_of_nodes = ([1, 2, 3, 4, 5, ] if self.auto_populate else[]) + self.list_of_nodes


class BuildLinkedStack(_BuildStack):
    def _create_stack(self):
        self._stack = LinkedStack()

    def build(self):
        for node in self.list_of_nodes:
            self._stack.push(node)

        return self._stack