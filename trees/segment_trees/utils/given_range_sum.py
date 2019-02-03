# Problem Statement
# https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/

from trees.segment_trees import BuildArraySegmentTree


class SegmentTreeOperation:
    def __init__(self, arr):
        self.segment_tree = BuildArraySegmentTree(arr).get_tree()
        self.input_arr = arr

    def get_given_range_sum(self, range_start_index: int, range_end_index: int):
        # Input value checks
        if range_end_index >= len(self.input_arr) or range_start_index < 0:
            raise IndexError('Start and End indexes should be in array range!')

        assert range_start_index <= range_end_index, 'Start index should be less than End index!'
        ##############################

        def _get_given_range_sum(node_index):
            node = self.segment_tree.list_of_nodes[node_index]
            if range_start_index <= node.low and range_end_index >= node.high:
                return node.data

            elif node.low > range_end_index or node.high < range_start_index:
                return 0

            return _get_given_range_sum(self.segment_tree.get_left_node_index(node_index)) + _get_given_range_sum(self.segment_tree.get_right_node_index(node_index))

        return _get_given_range_sum(self.segment_tree.root_index)

    def update_given_index_value(self, arr_index, new_val):
        if arr_index >= len(self.input_arr) or arr_index < 0:
            raise IndexError('Start and End indexes should be in array range!')

        value_diff = new_val - self.input_arr[arr_index]
        self.input_arr[arr_index] = value_diff
        # TODO: update segment tree


# driver code
def run():
    arr = [1, 3, 5, 7, 9, 11]
    segment_tree_operation = SegmentTreeOperation(arr)

    range_start = 2
    range_end = 4

    print(f'Sum of {arr} in range({range_start}, {range_end}) is: ')
    print(segment_tree_operation.get_given_range_sum(range_start, range_end))


if __name__ == '__main__':
    run()
