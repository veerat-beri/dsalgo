# Problem Statement
# https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/

from typing import List


class PairWithGivenSum:
    USE_SORTING = 'use_sorting'
    USE_HASHING = 'use_hashing'

    def __init__(self, arr: List, unique=False, only_one_result=False, method=USE_HASHING):
        self.arr = arr
        self.arr_len = len(self.arr)
        self.only_unique_pairs = unique
        self.only_one_result = only_one_result
        self.method = method if not unique else self.USE_SORTING

    # Hash based Approach
    def _using_hashing(self, required_sum, arr_start_index=0):
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        hash_set = set()

        for arr_index in range(arr_start_index, self.arr_len):
            elem = self.arr[arr_index]
            another_no_in_pair = required_sum - elem

            if another_no_in_pair in hash_set:
                yield elem, another_no_in_pair

                if self.only_one_result:
                    break

            hash_set.add(elem)

    # Sorting based Approach
    def _using_sorting(self, required_sum):
        # Time Complexity: O(N*logN + N) ~ O(N*logN)
        # Space Complexity: O(1)
        self.arr.sort()

        start_index = 0
        end_index = len(self.arr) - 1
        latest_unique_pair_elem = set()

        while start_index < end_index:
            elem1 = self.arr[start_index]
            elem2 = self.arr[end_index]
            if elem1 + elem2 == required_sum:
                start_index += 1
                end_index -= 1

                if self.only_unique_pairs and latest_unique_pair_elem and elem2 in latest_unique_pair_elem and elem1 in latest_unique_pair_elem:
                    continue

                latest_unique_pair_elem = {elem1, elem2}
                yield elem1, elem2

                if self.only_one_result:
                    break

            elif elem1 + elem2 < required_sum:
                start_index += 1
            else:
                end_index -= 1

    def get_results(self, required_sum: int):
        return (self._using_sorting if self.method == self.USE_SORTING else self._using_hashing)(required_sum)


# driver code
def run():
    arr = [1, 1, 10, 5, 3, 8, 7, 15, 10]
    required_sum = 11

    print(f'Given arr: {arr}\n')
    print(f'Pairs with sum = {required_sum} are: ')
    for pair in PairWithGivenSum(
        arr,
        # unique=True,
        # only_one_result=True,
        method=PairWithGivenSum.USE_SORTING
    ).get_results(required_sum=required_sum):

        print(pair[0], pair[1])


if __name__ == '__main__':
    run()
