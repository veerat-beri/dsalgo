# Problem Statement
# https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/


from trees.segment_trees import BuildArraySegmentTree, ArraySegmentTree


def get_given_range_sum(arr, range_start: int, range_end: int):
    if not range_end >= len(arr) or not range_start <= 0:
        raise IndexError('Start and End indexes should be in array range!')

    assert range_start <= range_end, 'Start index should be less than End index!'

    range_start_index, range_end_index = range_start - 1, range_end - 1
    segment_tree = BuildArraySegmentTree(arr).get_tree()

    def _get_given_range_sum(node: ArraySegmentTree.ArraySegmentTreeNode):
        if range_start_index == node.low and range_end_index == node.high:
            return node

        mid = segment_tree.get_mid(node.low, node.high)
        # TODO: add here

    return _get_given_range_sum(segment_tree.root)


# driver code
def run():
    arr = [1, 3, 5, 7, 9, 11]
    range_start = 1
    range_end = 3

    print(f'Sum of {arr} in range({range_start}, {range_end}) is: ')
    print(get_given_range_sum(arr, range_start, range_end).data)


if __name__ == '__main__':
    run()
