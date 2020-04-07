# Problem Statement
# https://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/

# from sys import maxsize
#
#
# def maxPathSum(root):
#     def __max_sum(node):
#         if not node:
#             return 0
#
#         lft_tree_sum = __max_sum(node.left)
#         rgt_tree_sum = __max_sum(node.right)
#
#         max_subtree_sum = max(lft_tree_sum, rgt_tree_sum)
#         path_sum = max(node.data + max_subtree_sum, node.data)
#         __max_sum.max_path_sum = max(__max_sum.max_path_sum, path_sum, lft_tree_sum + rgt_tree_sum + node.data)
#         return path_sum
#
#     __max_sum.max_path_sum = -maxsize
#     __max_sum(root)
#     return __max_sum.max_path_sum


# Problem Statement
# https://www.geeksforgeeks.org/find-maximum-path-sum-two-leaves-binary-tree/
