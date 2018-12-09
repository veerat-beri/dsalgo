# Problem Statement
# https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/


from trees.segment_trees import BuildArraySegmentTree


def get_given_range_sum(arr, range_start: int, range_end: int):
    if not range_end >= len(arr) or not range_start <= 0:
        raise IndexError('Start and End indexes should be in array range!')

    if range_start > range_end:
        raise IndexError('Start index should be less than End index!')

    range_start_index, range_end_index = range_start - 1, range_end - 1
    segment_tree = BuildArraySegmentTree(arr)

    def _get_given_range_sum(node):
        if range_start_index == node.low and range_end_index == node.end:
            return node
        elif range_start_index >= node.low and range_end_index <=



    return _get_given_range_sum()
