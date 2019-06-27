# Problem Statement
# https://www.geeksforgeeks.org/count-triplets-with-sum-smaller-that-a-given-value/

from typing import List


class TripletExists:
    def __init__(self, arr: List, max_triplet_sum: int):
        self.arr = arr
        self.max_triplet_sum = max_triplet_sum

    def _using_sorting(self):
        result_count = 0
        self.arr.sort()
        for primary_arr_index in range(len(self.arr) - 1):
            secondary_arr_index = primary_arr_index
            ternary_arr_index = len(self.arr) - 1
            while secondary_arr_index < ternary_arr_index:
                triplet_sum = self.arr[secondary_arr_index] + self.arr[primary_arr_index] + self.arr[ternary_arr_index]
                if triplet_sum < self.max_triplet_sum:
                    result_count += 1
                    secondary_arr_index += 1
                else:
                    ternary_arr_index -= 1
        return result_count

    def check_triplet_exists(self, **kwargs):
        return self._using_sorting()


# driver code
def run():
    arr = [-2, 0, 1, 3, ]
    triplet_sum = 2
    required_triplets_count = TripletExists(arr, triplet_sum)


if __name__ == '__main__':
    run()
