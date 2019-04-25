# Problem Statement
# https://www.geeksforgeeks.org/merge-sort/
from arrays.services import swap_arr_elem


class MergeSort:
    def __init__(self, arr: []):
        self.input_arr = arr

    def _get_sorted_merged_arrays(self, low: int, mid: int, high: int):
        arr1_index = low
        arr2_index = mid + 1
        out_arr_index = low

        # breakpoint()
        while arr1_index <= mid and arr2_index <= high:
            # if self.input_arr[arr1_index] < self.input_arr[arr2_index]:
            if self.input_arr[arr1_index] > self.input_arr[arr2_index]:
                swap_arr_elem(arr1_index, arr2_index, self.input_arr)
                # self.input_arr[out_arr_index] = self.input_arr[arr1_index]
                arr1_index += 1
            # else:
            #     swap_arr_elem(arr1_index, arr2_index, self.input_arr)
            #     # self.input_arr[out_arr_index] = self.input_arr[arr2_index]
            #     arr2_index += 1
            out_arr_index += 1

        # breakpoint()
        # while arr1_index <= mid:
        #     print('yes, in first')
        #     self.input_arr[out_arr_index] = self.input_arr[arr1_index]
        #     arr1_index += 1
        #     out_arr_index += 1
        #
        # while arr2_index <= high:
        #     print('yes in second')
        #     self.input_arr[out_arr_index] = self.input_arr[arr2_index]
        #     arr2_index += 1
        #     out_arr_index += 1


        print(low, mid, high, self.input_arr)
        # breakpoint()

    def sort_arr(self, low, high):
        if low >= high:
            return

        mid = (high - low)//2 + low

        self.sort_arr(low, mid)
        self.sort_arr(mid + 1, high)
        self._get_sorted_merged_arrays(low, mid, high)


# driver code
def run():
    arr = [38, 27, 43, 3, 9, 82, 10, ]
    arr = [12, 11, 13, 5, 6, 7, ]

    print(f'Array before sort: {arr}')
    MergeSort(arr).sort_arr(0, len(arr) - 1)
    print(f'Array after sort: {arr}')


if __name__ == '__main__':
    run()
