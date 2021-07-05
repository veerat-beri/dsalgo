from collections import deque


class Graph:
    DIRECTED = 'directed'
    UNDIRECTED = 'undirected'

    class Vertex:
        __slots__ = '_element'

        def __init__(self, data):
            self._element = data

        def __hash__(self):
            return hash(id(self))

        @property
        def element(self):
            return self._element

    class Edge:
        __slots__ = '_element', '_origin', '_destination'

        def __init__(self, source_vertex, destination_vertex, element=None):
            self._origin = source_vertex
            self._destination = destination_vertex
            self._element = element

        def __hash__(self):
            return hash((self._origin, self._destination))

        def opposite(self, vertex):
            return self._destination if vertex is self._origin else self._origin

        def endpoints(self):
            return self._origin, self._destination

        @property
        def element(self):
            return self._element

    def __init__(self, directed=False):
        self._outgoing_edges = {}
        self._incoming_edges = {} if directed else self._outgoing_edges

    @property
    def is_directed(self):
        return self._incoming_edges is not self._outgoing_edges

    @property
    def vertex_count(self):
        return len(self._outgoing_edges)

    def vertices(self):
        return list(self._outgoing_edges)

    @property
    def edge_count(self):
        total_edges = sum(len(self._outgoing_edges[vertex]) for vertex in self._outgoing_edges)
        return total_edges//2 if self.is_directed else total_edges

    # def get_new_node(self, node_data):
    #     return self.GraphNode(node_data)
    #
    # def add_edge(self, from_node_data, to_node_data):
    #     from_node = self.GraphNode(from_node_data)
    #     to_node = self.GraphNode(to_node_data)
    #     from_node._ajc.append(to_node)
    #     to_node._ajc.append(from_node)
    #     # self.graph[].append(to_node)
    #     self.graph[from_node._data] = from_node
    #     self.graph[to_node._data] = to_node
    #
    # def bfs(self, source_node=None):
    #     visited_nodes = set()
    #     bfs_queue = deque()
    #     if source_node is None:
    #         source_node = self.graph[0]
    #
    #     bfs_queue.append(source_node)
    #     while bfs_queue:
    #         node = bfs_queue.popleft()
    #         visited_nodes.add(node)
    #         yield node
    #         for adj_node in node._ajc:
    #             if adj_node not in visited_nodes:
    #                 bfs_queue.append(adj_node)
    #
    # def shortest_path(self, source_node: GraphNode):
    #     visited_nodes = set()
    #     bfs_queue = deque()
    #     if source_node is None:
    #         source_node = self.graph[0]
    #
    #     bfs_queue.append((source_node, 0))
    #     while bfs_queue:
    #         node, level = bfs_queue.popleft()
    #         visited_nodes.add(node)
    #         yield (node, level)
    #         for adj_node in node._ajc:
    #             if adj_node not in visited_nodes:
    #                 bfs_queue.append((adj_node, level + 1))
