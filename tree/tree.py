
class TreeNode:
    def __init__(self, data=None, **kwargs):
        self.data = data
        self.left = TreeNode()
        self.right = TreeNode()


class Tree:
    def root(self):
        raise NotImplementedError('Has to be Implemented by sub class')

    def parent(self):
        raise NotImplementedError('Has to be Implemented by sub class')

    def number_of_children(self):
        raise NotImplementedError('Has to be Implemented by sub class')

    def children(self):
        raise NotImplementedError('Has to be Implemented by sub class')

    def __len__(self, other):
        raise NotImplementedError('Has to be Implemented by sub class')

    # Concrete methods implementations
    def is_root(self, node):
        return self.root() == node

    def is_leaf(self, node):
        return bool(self.number_of_children())

    def is_empty(self):
        return bool(len(self))
