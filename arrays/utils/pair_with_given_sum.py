# Problem Statement
# https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/


def check_pair_exists(arr, sum_of_pair):
    hash_set = set()
    for index in range(len(arr)):
        elem = arr[index]
        another_no_in_pair = sum_of_pair - elem

        if another_no_in_pair > 0 and (another_no_in_pair in hash_set):
            return elem, another_no_in_pair
        hash_set.add(elem)


# driver code
def run():
    arr = [1, 5, 3, 8, 7, 15]
    sum_of_pair = 11
    pair = check_pair_exists(arr, sum_of_pair)
    if pair:
        print('Yes, pair exist:({}, {}) with sum = {}'.format(pair[0], pair[1], sum_of_pair))
    else:
        print('No pair exists with given sum')


if __name__ == '__main__':
    run()
