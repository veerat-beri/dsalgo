# class LinkedBinaryTreeTraversalMixin:
#     BFS = 'BFS'
#     DFS = 'DFS'
#
#     TRAVERSAL_CHOICES = (
#         (BFS, 'BREADTH FIRST SEARCH'),
#         (DFS, 'DEPTH FIRST SEARCH'),
#     )
#
#     @set_default_node
#     def bfs(self, node):
#         if node is None:
#             raise Exception('Tree is empty!')
#
#         bfs_queue = deque()  # Used as Queue
#         bfs_queue.append((node, 0))
#
#         while bfs_queue:
#             node, node_level = bfs_queue.popleft()
#             yield node, node_level
#             ###############
#             # 1st Approach
#             # left_child = self.left(node)
#             # right_child = self.right(node)
#             # if left_child is not None:
#             #     bfs_queue.append(left_child)
#             # if right_child is not None:
#             #     bfs_queue.append(right_child)
#             ###############
#             # 2nd Approach
#             for child in self.children(node):
#                 bfs_queue.append((child, node_level + 1))
#             ###############
