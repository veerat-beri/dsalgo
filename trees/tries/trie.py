# Problem Statement
# https://www.geeksforgeeks.org/trie-insert-and-search/

from trees.tree import BinaryTree


class Trie(BinaryTree):
    # for only small english chars
    DEFAULT_TRIE_NODE_CHILDREN_COUNT = 26

    class TrieNode(BinaryTree.BinaryTreeNode):
        def __init(self, **kwargs):
            self.children_count = self.TRIE_NODE_CHILDREN_COUNT
            child_nodes = [] * self.children_count

    def __init__(self, node_children_count: int = None, **kwargs):
        self.TRIE_NODE_CHILDREN_COUNT = node_children_count or self.DEFAULT_TRIE_NODE_CHILDREN_COUNT
