
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

    def number_of_children(self, node: TreeNode):
        raise NotImplementedError('Has to be Implemented by sub class')

    def children(self, node: TreeNode):
        raise NotImplementedError('Has to be Implemented by sub class')

    def __len__(self, other):
        raise NotImplementedError('Has to be Implemented by sub class')

    # Concrete methods implementations
    def is_root(self, node):
        return self.root() == node

    def is_leaf(self, node):
        return self.number_of_children(node) == 0

    def is_empty(self):
        return len(self) == 0

    def height(self, node: TreeNode):
        # 1st Approach
        # if not node:
        #     return 0
        # left_subtree_height = self.height(node.left)
        # right_subtree_height = self.height(node.right)
        # return 1 + max(left_subtree_height, right_subtree_height)
        ###############

        # 2nd Approach
        if self.is_leaf(node):
            return 0
        return 1 + max(self.height(node) for node in self.children(node))
        ###############