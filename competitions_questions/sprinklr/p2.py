# Problem Statement
#


#############################################################################################################
# SOLUTION
#############################################################################################################
node_dest_cache = {}


def get_terminating_node(node_index, nodes_connection_arr):
    visited_nodes = set()
    while nodes_connection_arr[node_index-1]:
        if nodes_connection_arr[node_index - 1] in node_dest_cache:
            return node_dest_cache[nodes_connection_arr[node_index - 1]]
        if node_index in visited_nodes:
            return None
        visited_nodes.add(node_index)
        node_index = nodes_connection_arr[node_index-1]
    return node_index


def process_query(query_type, node_index, nodes_connection_arr):
    global node_dest_cache
    if query_type == 1:
        terminating_node = node_dest_cache[node_index] if node_index in node_dest_cache else get_terminating_node(node_index, nodes_connection_arr)

        if terminating_node is None:
            print('LOOP')
        else:
            print(terminating_node)

        node_dest_cache[node_index] = terminating_node
    else:
        nodes_connection_arr[node_index - 1] = 0
        node_dest_cache = {}


total_nodes = int(input())
nodes_connection_arr = list(map(int, input().strip().split()))
total_queries = int(input())

for _ in range(total_queries):
    query_type, node = list(map(int, input().strip().split()))
    process_query(query_type, node, nodes_connection_arr)
