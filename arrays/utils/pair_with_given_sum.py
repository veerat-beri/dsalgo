# Problem Statement
# https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/

from typing import List


class PairExists:
    def __init__(self, arr: List, sum_of_pair: int):
        self.arr = arr
        self.sum_of_pair = sum_of_pair

    # Hash based Approach
    def _using_hashing(self):
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        hash_set = set()
        for index in range(len(self.arr)):
            elem = self.arr[index]
            another_no_in_pair = self.sum_of_pair - elem

            if another_no_in_pair > 0 and (another_no_in_pair in hash_set):
                return elem, another_no_in_pair
            hash_set.add(elem)

    def _using_sorting(self):
        # Time Complexity: O(N*logN + N)
        # Space Complexity: O(1)
        self.arr.sort()
        start_index = 0
        end_index = len(self.arr) - 1
        while start_index < end_index:
            elem1 = self.arr[start_index]
            elem2 = self.arr[end_index]
            if elem1 + elem2 == self.sum_of_pair:
                return self.arr[start_index], self.arr[end_index]
            elif elem1 + elem2 < self.sum_of_pair:
                start_index += 1
            else:
                end_index -= 1

    def check_pair_exists(self, **kwargs):
        if kwargs.get('use_sorting'):
            return self._using_sorting()
        return self._using_hashing()


# driver code
def run():
    arr = [1, 5, 3, 8, 7, 15]
    sum_of_pair = 11
    pair = PairExists(arr, sum_of_pair).check_pair_exists()
    # pair = PairExists(arr, sum_of_pair).check_pair_exists(use_sorting=True)
    if pair:
        print(f'Yes, pair exist:({pair[0]}, {pair[1]}) with sum = {sum_of_pair}')
    else:
        print(f'No pair exists with given sum({sum_of_pair})')


if __name__ == '__main__':
    run()
