# Problem Statement
# https://www.geeksforgeeks.org/merge-sort/

from arrays.utils.merge_k_sorted_arrays import MergeKSortedArrays


class MergeSort:
    def __init__(self, arr: []):
        self.output_arr = []
        self.input_arr = arr

    def get_sorted_merged_arrays(self, low: int, mid: int, high: int):
        arr1_start_index = low
        arr_2_start_index = high - mid + 1
        # while arr1_index <= mid_index and


    def get_sorted_arr(self, arr: [], low, high):
        # def _get_sorted_arr(low, high, ):
        if low >= high:
            return

        mid = (high - low)//2 + low
        self.get_sorted_arr(arr, low, mid)
        self.get_sorted_arr(arr, mid + 1, high)





# driver code
def run():
    pass


if __name__ == '__main__':
    run()
