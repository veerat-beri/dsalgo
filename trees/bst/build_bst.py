from trees import BuildLinkedBinaryTree


class BuildLinkedBinarySearchTree(BuildLinkedBinaryTree):
    def _build_tree(self):
        if self.list_of_nodes:
            if self._tree.is_empty():
                root_node = self._tree.add_root(self.list_of_nodes[0])
                index = 1
                bfs_queue = deque()
                bfs_queue.append(root_node)
                while index <= len(self.list_of_nodes) - 1:
                    root_node = bfs_queue.popleft()
                    self._tree.add_left_child(root_node, self.list_of_nodes[index])
                    index += 1
                    bfs_queue.append(self._tree.left(root_node))

                    if index == len(self.list_of_nodes):
                        break

                    self._tree.add_right_child(root_node, self.list_of_nodes[index])
                    index += 1
                    bfs_queue.append(self._tree.right(root_node))
