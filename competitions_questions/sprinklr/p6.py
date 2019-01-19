# Problem Statement
#

#############################################################################################################
# SOLUTION
#############################################################################################################
from collections import deque


def get_all_cities_dist(start_node=0):
    global roads_connection, costs_dict
    distance = {}
    bfs_queue = deque()
    bfs_queue.append(start_node)
    distance[0] = [(0, 0, [])]  # (num_of_hops, sum_of_cost)
    visited_nodes = set()
    while bfs_queue:
        node = bfs_queue.popleft()
        for neighbour in roads_connection[node]:
            if (node, neighbour) in visited_nodes:
                continue
            neighbour_dist = distance.get(neighbour)
            if neighbour_dist:
                neighbour_dist.append((distance[node][-1][0] + 1, distance[node][-1][1] + costs_dict[node, neighbour], distance[node][-1][2] + [costs_dict[node, neighbour]]))
            else:
                distance[neighbour] = [(distance[node][-1][0] + 1, distance[node][-1][1] + costs_dict[node, neighbour], distance[node][-1][2] + [costs_dict[node, neighbour]])]

            bfs_queue.append(neighbour)
            visited_nodes.add((node, neighbour))
    return distance


def process_distance(all_cities_dist):
    global total_cities, total_wildcards
    print(0, end=' ')
    for city in range(1, total_cities):
        # if city_dist_cal[0][0] <= total_wildcards:
        #     print(0, end=' ')
        for city_dist in all_cities_dist[city]:
            if city_dist[0] <= total_wildcards:
                print(0, end=' ')
                break
        else:
            print(sum(sorted(sorted(all_cities_dist[city], key=lambda x: x[1])[0][2], reverse=True)[total_wildcards:]), end=' ')


total_cities, total_roads, total_wildcards = list(map(int, input().strip().split()))
roads_connection = [[] for _ in range(total_cities)]
costs_dict = {}  # (1, 2): 3

for _ in range(total_roads):
    start_node, end_node, road_tax = list(map(int, input().strip().split()))
    roads_connection[start_node - 1].append(end_node - 1)
    costs_dict[(start_node - 1, end_node - 1)] = road_tax

all_cities_dist = get_all_cities_dist()
process_distance(all_cities_dist)



