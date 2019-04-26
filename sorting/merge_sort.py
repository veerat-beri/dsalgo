# Problem Statement
# https://www.geeksforgeeks.org/merge-sort/
from arrays.services import swap_arr_elem


class MergeSort:
    def __init__(self, arr: []):
        self.input_arr = arr

    def _get_sorted_merged_arrays(self, low: int, mid: int, high: int):
        left_array = self.input_arr[low: mid + 1]
        right_arr = self.input_arr[mid + 1: high + 1]

        arr1_index = 0
        arr2_index = 0
        out_arr_index = low

        print('single iteraton', left_array, right_arr, low, mid, high)
        while arr1_index <= mid - low and arr2_index <= high - mid - 1:


            print(arr1_index, arr2_index)
            if left_array[arr1_index] < right_arr[arr2_index]:
                self.input_arr[out_arr_index] = left_array[arr1_index]
                arr1_index += 1
            else:
                self.input_arr[out_arr_index] = right_arr[arr2_index]
                arr2_index += 1
            out_arr_index += 1

        breakpoint()
        print(out_arr_index)
        while arr1_index <= mid - low:
            self.input_arr[out_arr_index] = self.input_arr[arr1_index]
            arr1_index += 1
            out_arr_index += 1

        while arr2_index <= high - mid - 1:
            self.input_arr[out_arr_index] = self.input_arr[arr2_index]
            arr2_index += 1
            out_arr_index += 1


        print(self.input_arr)
        # print(low, mid, high, self.input_arr)
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
