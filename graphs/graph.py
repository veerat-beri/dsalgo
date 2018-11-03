from collections import deque


class Graph:
    class GraphNode:
        def __init__(self, data):
            self._data = data
            self._ajc = []

    def __init__(self, no_of_nodes=1):
        self.graph = {}

    def add_edge(self, from_node_data, to_node_data):
        from_node = self.GraphNode(from_node_data)
        to_node = self.GraphNode(to_node_data)
        from_node._ajc.append(to_node)
        to_node._ajc.append(from_node)
        # self.graph[].append(to_node)
        self.graph[from_node._data] = from_node
        self.graph[to_node._data] = to_node

    def bfs(self, source_node=None):
        visited_nodes = set()
        bfs_queue = deque()
        if source_node is None:
            source_node = self.graph[0]

        bfs_queue.append(source_node)
        while bfs_queue:
            node = bfs_queue.popleft()
            visited_nodes.add(node)
            yield node
            for adj_node in node._ajc:
                if adj_node not in visited_nodes:
                    bfs_queue.append(adj_node)

    def shortest_path(self, source_node: GraphNode):
        visited_nodes = set()
        bfs_queue = deque()
        if source_node is None:
            source_node = self.graph[0]

        bfs_queue.append((source_node, 0))
        while bfs_queue:
            node, level = bfs_queue.popleft()
            visited_nodes.add(node)
            yield (node, level)
            for adj_node in node._ajc:
                if adj_node not in visited_nodes:
                    bfs_queue.append((adj_node, level + 1))

