class ZeroSubArray:
    def __init__(self, arr: []):
        self.arr = arr
        self.arr_len = len(arr)

    # Problem Statement
    # https://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/
    def check_zero_sum_sub_arr_exists(self):
        prefix_sum = set()
        arr_sum_till_point = 0

        # To handle case like: [4, -2, -1, -1, -1], where prefix sum is itself zero.
        prefix_sum.add(0)

        for elem in self.arr:
            arr_sum_till_point += elem
            if arr_sum_till_point in prefix_sum:
                return True
            prefix_sum.add(arr_sum_till_point)
        return False

    ############################################################
    # Problem Statement
    # https://www.geeksforgeeks.org/find-the-largest-subarray-with-0-sum/
    def _get_arr_elem(self, index):
        """
        Overridable function, to modify sorted_arrays-elem
        :param index:
        :return:
        """
        return self.arr[index]

    def get_zero_sum_sub_arr(self):
        indexed_prefix_sum = {}
        arr_sum_till_point = 0
        max_length_zero_sum_sub_arr_indexes = ()
        zero_sum_sub_arr_max_length = 0
        for index in range(self.arr_len):
            arr_sum_till_point += self._get_arr_elem(index)
            if arr_sum_till_point == 0:
                zero_sum_sub_arr_max_length = index + 1
                max_length_zero_sum_sub_arr_indexes = (0, index)

            if arr_sum_till_point in indexed_prefix_sum:
                if zero_sum_sub_arr_max_length < index - indexed_prefix_sum[arr_sum_till_point]:
                    zero_sum_sub_arr_max_length = index - indexed_prefix_sum[arr_sum_till_point]
                    max_length_zero_sum_sub_arr_indexes = (indexed_prefix_sum[arr_sum_till_point] + 1, index)

            elif arr_sum_till_point != 0:
                indexed_prefix_sum[arr_sum_till_point] = index
        return zero_sum_sub_arr_max_length, max_length_zero_sum_sub_arr_indexes


# driver code
def run():
    # sorted_arrays = [1, 1, 0, 0, ]
    # sorted_arrays = [4, -2, -1, -1, -1, 1]
    arr = [15, -2, 2, -1, 1, 10, -5, -3, -1, -1, 0, ]
    # sorted_arrays = [15, -2, 2, -1, 1, 20, 10, -5, -3, -1, -1, 0, ]

    print(f'Given sorted_arrays: {arr}')
    ###############
    # Check whether zero sum sub-array exists or not
    do_zero_sum_sub_arr_exists = ZeroSubArray(arr).check_zero_sum_sub_arr_exists()
    message = 'Sub-array with zero sum ' + ('exists' if do_zero_sum_sub_arr_exists else 'do not exists')
    print(message)

    ###############
    sub_arr_len, sub_arr_indexes = ZeroSubArray(arr).get_zero_sum_sub_arr()
    if sub_arr_len:
        print(f'\nMax Length({sub_arr_len}) Sub-array with zero sum: ',
              arr[sub_arr_indexes[0]: sub_arr_indexes[1] + 1], sep='\n')
    else:
        print('Sub-array with zero sum do not exists!')


if __name__ == '__main__':
    run()
