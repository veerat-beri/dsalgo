# Problem Statement
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/


# Recursive Approach
def get_max_total_value(bag_weight_capacity: int, weight_list: [], values_list: []):
    if len(weight_list) != len(values_list):
        raise Exception('weight-list and value-list are not of same length!')

    def _get_max_total_value(list_untraversed_len, bag_weight_capacity_left):
        if list_untraversed_len == 0 or bag_weight_capacity_left == 0:
            return 0
        if weight_list[list_untraversed_len - 1] <= bag_weight_capacity_left:
            return max(
                values_list[list_untraversed_len - 1] +
                _get_max_total_value(list_untraversed_len - 1, bag_weight_capacity_left - weight_list[list_untraversed_len - 1]),
                _get_max_total_value(list_untraversed_len - 1, bag_weight_capacity_left),
            )
        return _get_max_total_value(list_untraversed_len - 1, bag_weight_capacity_left),

    return _get_max_total_value(len(values_list), bag_weight_capacity)
##########################################################################################


# driver code
def run():
    weight_list = [10, 20, 30]
    values_list = [60, 100, 120]
    bag_weight_limit = 50
    max_total_value = get_max_total_value(bag_weight_limit, weight_list, values_list)
    print(f'Max value for max-weight({bag_weight_limit}) is: ', max_total_value)


if __name__ == '__main__':
    run()


