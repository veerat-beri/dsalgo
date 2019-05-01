# Problem Statement
# https://www.geeksforgeeks.org/merge-sort/


class MergeSort:
    def __init__(self, arr: []):
        self.input_arr = arr

    @classmethod
    def update_arr(cls, elem, arr: [], arr_index: int = None):
        if arr_index:
            arr[arr_index] = elem
        else:
            arr.appemd(elem)

    @classmethod
    def merge_sorted_arrays(cls, left_array, right_arr, out_arr: [], out_arr_index: int = None):
        arr1_index, arr2_index, out_arr_index = 0, 0, out_arr_index

        while arr1_index < len(left_array) and arr2_index < len(right_arr):
            if left_array[arr1_index] < right_arr[arr2_index]:
                cls.update_arr(left_array[arr1_index], out_arr, out_arr_index)
                # out_arr[out_arr_index] = left_array[arr1_index]
                arr1_index += 1
            else:
                # out_arr[out_arr_index] = right_arr[arr2_index]
                cls.update_arr(right_arr[arr2_index], out_arr, out_arr_index)
                arr2_index += 1
            out_arr_index += 1

        while arr1_index < len(left_array):
            # self.input_arr[out_arr_index] = left_array[arr1_index]
            out_arr[out_arr_index] = left_array[arr1_index]
            arr1_index += 1
            out_arr_index += 1

        while arr2_index < len(right_arr):
            # self.input_arr[out_arr_index] = right_arr[arr2_index]
            out_arr[out_arr_index] = right_arr[arr2_index]
            arr2_index += 1
            out_arr_index += 1

    def _merge_sorted_arrays(self, low: int, mid: int, high: int):
        left_array = self.input_arr[low: mid + 1]
        right_arr = self.input_arr[mid + 1: high + 1]
        self.merge_sorted_arrays(left_array, right_arr, low, self.input_arr)

    def sort_arr(self, low, high):
        if low >= high:
            return

        mid = (high - low)//2 + low

        self.sort_arr(low, mid)
        self.sort_arr(mid + 1, high)
        self._merge_sorted_arrays(low, mid, high)


# driver code
def run():
    arr = [38, 27, 43, 3, 9, 82, 10, ]
    # sorted_arrays = [12, 11, 13, 5, 6, 7, ]

    print(f'Array before sort: {arr}')
    MergeSort(arr).sort_arr(0, len(arr) - 1)
    print(f'Array after sort: {arr}')


if __name__ == '__main__':
    run()
