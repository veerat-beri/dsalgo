# Problem Statement
# https://leetcode.com/articles/recover-binary-search-tree/


class RecoverBST:
    def __init__(self):
        pass

    previous_node_data = None

    def _is_bst_using_inorder(node):
        nonlocal previous_node_data
        if node is None:
            return True

        if not _is_bst_using_inorder(bt.left(node)):
            return False

        if previous_node_data and previous_node_data > node.data:
            return False

        previous_node_data = node.data

        return _is_bst_using_inorder(bt.right(node))
    def get_correct_bst(self):


# driver code
def run():
    pass


if __name__ == '__main__':
    run()
