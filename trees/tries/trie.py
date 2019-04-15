# Problem Statement
# https://www.geeksforgeeks.org/trie-insert-and-search/


from strings.service import get_relative_ascii, get_relative_char
from trees.tree import BinaryTree


class Trie:
    # either small or large Alphabet set
    DEFAULT_TRIE_NODE_CHILDREN_COUNT = 26

    class TrieNode(BinaryTree.BinaryTreeNode):
        def __init__(self, **kwargs):
            self.child_nodes = [None] * Trie.DEFAULT_TRIE_NODE_CHILDREN_COUNT
            self.is_end_node = False

    def __init__(self, node_children_count: int = None, **kwargs):
        self.TRIE_NODE_CHILDREN_COUNT = node_children_count or self.DEFAULT_TRIE_NODE_CHILDREN_COUNT
        self._root = self.TrieNode()

    def get_new_node(self):
        return self.TrieNode()

    def insert(self, word: str):
        word_len = len(word)

        # Recursive Approach
        def _insert(trie_node: Trie.TrieNode, word_index: int):
            if not trie_node.child_nodes[get_relative_ascii(word[word_index])]:
                trie_node.child_nodes[get_relative_ascii(word[word_index])] = self.get_new_node()

            if word_index + 1 == word_len:
                node = trie_node.child_nodes[get_relative_ascii(word[word_index])]
                node.is_end_node = True
                # trie_node.is_end_node = True
                return

            return _insert(trie_node.child_nodes[get_relative_ascii(word[word_index])], word_index + 1)

        ##############################
        # Iterative Approach

        ##############################
        _insert(self.root(), 0)

    def print_trie(self):
        def _print_trie(trie_node: Trie.TrieNode, word_so_far):
            for node_index in range(self.DEFAULT_TRIE_NODE_CHILDREN_COUNT):
                if trie_node.is_end_node:
                    print(word_so_far + get_relative_char(node_index) + ', ')

                if trie_node.child_nodes[node_index]:
                    _print_trie(trie_node.child_nodes[node_index], word_so_far + get_relative_char(node_index))

        _print_trie(self.root(), '')

    def root(self):
        return self._root


# driver code
def run():
    words_to_be_inserted = ['the', 'a', 'there', 'anaswe', 'any', 'by', 'their']
    words_to_be_inserted = ['any', 'anaswe', ]
    trie = Trie()
    for word in words_to_be_inserted:
        trie.insert(word)

    trie.print_trie()


if __name__ == '__main__':
    run()
