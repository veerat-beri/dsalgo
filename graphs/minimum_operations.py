from collections import deque

# graph = Graph()
# # for index in range(1, 6):
# #     graph.add_edge(index)
#
# n0 = graph.GraphNode(0)
# n1 = graph.GraphNode(2)
# n2 = graph.GraphNode(2)
# n3 = graph.GraphNode(2)
# n4 = graph.GraphNode(2)
# n5 = graph.GraphNode(2)


x = 4
y = 7

bfs_queue = deque()
bfs_queue.append((x, 0))
found = False
visited_nodes = set()


def safe_append(node, level):
    if node not in visited_nodes:
        # if node(range logic)
        bfs_queue.append((node, level + 1))


while bfs_queue:
    node, level = bfs_queue.popleft()
    if node == y:
        print('No of operation:', level)
        break
    visited_nodes.add(node)
    safe_append(node*2, level + 1)
    safe_append(node-1, level + 1)



