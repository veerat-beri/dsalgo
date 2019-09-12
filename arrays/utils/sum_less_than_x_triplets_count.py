# Problem Statement
# https://www.geeksforgeeks.org/count-triplets-with-sum-smaller-that-a-given-value/

from typing import List


class TripletExists:
    def __init__(self, arr: List, max_triplet_sum: int):
        self.arr = arr
        self.max_triplet_sum = max_triplet_sum
        self.arr_len = len(self.arr)

    def _using_sorting(self):
        result_count = 0
        self.arr.sort()
        for primary_arr_index in range(self.arr_len - 2):
            secondary_arr_index = primary_arr_index + 1
            ternary_arr_index = self.arr_len - 1
            while secondary_arr_index < ternary_arr_index:
                triplet_sum = self.arr[secondary_arr_index] + self.arr[primary_arr_index] + self.arr[ternary_arr_index]
                if triplet_sum < self.max_triplet_sum:
                    # If this triplet sum is less than max_sum, then all other triplets
                    # which are of type (pr_index, sec_index + n, tern_index) would also satisfy the condition
                    result_count += ternary_arr_index - secondary_arr_index
                    secondary_arr_index += 1
                else:
                    ternary_arr_index -= 1
        return result_count

    def get_triplets_count(self, **kwargs):
        return self._using_sorting()


# driver code
def run():
    # arr = [-2, 0, 1, 3, ]
    # max_triplet_sum = 2
    arr = [5, 1, 3, 4, 7, ]
    max_triplet_sum = 12
    triplets_count = TripletExists(arr, max_triplet_sum).get_triplets_count()
    print(f'Given array: {arr}')
    print(f'Triplets count with sum less than={max_triplet_sum} is: {triplets_count}')


if __name__ == '__main__':
    run()
