# Problem Statement
# https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/

hash_set = set()


def check_pair_exists(arr, sum_of_pair):
    for index in range(len(arr)):
        elem = arr[index]
        another_no_in_pair = sum_of_pair - elem

        if another_no_in_pair > 0 and (another_no_in_pair in hash_set):
            print('Yes, pair exist:({}, {}) with sum = {}'.format(elem, another_no_in_pair, sum_of_pair))
            return

        hash_set.add(elem)


# driver code
arr = [1, 5, 3, 8, 7, 15]
sum_of_pair = 11
check_pair_exists(arr, sum_of_pair)
