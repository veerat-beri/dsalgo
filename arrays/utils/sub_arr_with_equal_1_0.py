from arrays.utils.sub_arr_with_zero_sum import ZeroSubArray


class BinaryArray(ZeroSubArray):
    def _get_arr_elem(self, index):
        return 1 if self.arr[index] else -1

    # Problem Statement
    # https://www.geeksforgeeks.org/largest-subarray-with-equal-number-of-0s-and-1s/
    def get_equal_0_1_longest_sub_arr(self):
        return self.get_zero_sum_sub_arr()


# driver code
def run():
    binary_arr = [1, 0, 1, 1, 1, 0, 0, ]
    print(f'Given arr: {binary_arr}')
    sub_arr_len, sub_arr_indexes = BinaryArray(binary_arr).get_equal_0_1_longest_sub_arr()
    print(f'\nMax Length({sub_arr_len}) Sub-array with zero sum: ',
          binary_arr[sub_arr_indexes[0]: sub_arr_indexes[1] + 1], sep='\n')


if __name__ == '__main__':
    run()
