# Problem Statement
# https://www.geeksforgeeks.org/find-length-of-loop-in-linked-list/


from linkedlists import SinglyLinkedList, BuildSinglyLinkedListWithLoop
from linkedlists.utils import check_loop_exists


def get_ll_loop_len(node_in_loop: SinglyLinkedList.Node):
    current_node = node_in_loop
    visited_nodes = set()
    loop_len = 0

    while current_node:
        if current_node in visited_nodes:
            break
        visited_nodes.add(current_node)
        loop_len += 1
        current_node = current_node.next

    return loop_len


# driver code
def run():
    singly_ll = BuildSinglyLinkedListWithLoop(auto_populate=True).get_ll()
    print('Length of loop in given ll is: ', get_ll_loop_len(check_loop_exists(singly_ll)[1]))


if __name__ == '__main__':
    run()
