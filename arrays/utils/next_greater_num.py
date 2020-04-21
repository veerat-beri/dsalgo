# Problem Statement
# https://www.geeksforgeeks.org/find-next-greater-number-set-digits/


from arrays.services import swap_arr_elem


def get_next_greater_num(input_num: [], use_time_optimised=False):
    num = input_num[:]
    num_len = len(num)

    ############################################################
    # Time complexity: O(N * log2 N + 2N)
    # Space Complexity: O(1)
    def _get_swapping_indexes():
        pivot_index = -1
        for arr_index in range(num_len - 2, -1, -1):
            if num[arr_index] < num[arr_index + 1]:
                pivot_index = arr_index
                break

        if pivot_index == -1:
            return None, None

        next_greater_digit_index = pivot_index + 1

        for arr_index in range(pivot_index + 2, num_len):
            elem = num[arr_index]
            if num[next_greater_digit_index] > elem > num[pivot_index]:
                next_greater_digit_index = arr_index

        return pivot_index, next_greater_digit_index

    ############################################################
    # Time complexity: O(N * log2 N + N)
    # Space Complexity: O(N)
    # def _get_min(num: [], arr_index: int, min_so_far_list: []):
    #     if min_so_far_list[arr_index + 1][0] > num[arr_index]:
    #         return num[arr_index], arr_index
    #     return min_so_far_list[arr_index + 1]
    #
    # def _get_swapping_indexes_TO():
    #     pivot_index = -1
    #     min_so_far_list = [0] * num_len
    #     min_so_far_list[-1] = (num[-1], num_len - 1)
    #
    #     for arr_index in range(num_len - 2, -1, -1):
    #         if num[arr_index] < num[arr_index + 1]:
    #             pivot_index = arr_index
    #             break
    #         min_so_far_list[arr_index] = _get_min(num, arr_index, min_so_far_list)
    #
    #     if pivot_index == -1:
    #         return None, None
    #
    #     return pivot_index, min_so_far_list[pivot_index + 1][1]

    ############################################################

    # executing_func = _get_swapping_indexes_TO if use_time_optimised else _get_swapping_indexes
    executing_func = _get_swapping_indexes
    pivot_index, swapping_index = executing_func()

    if pivot_index is None:
        return

    swap_arr_elem(pivot_index, swapping_index, num)
    num[pivot_index + 1:] = sorted(num[pivot_index + 1:])

    return ''.join(list(map(str, num)))


# driver code
def run():
    # num = '218765'
    num = '28765'
    # num = '321'
    num = '231'
    num_arr = list(map(int, num))
    next_greater_num = get_next_greater_num(num_arr)
    # next_greater_num = get_next_greater_num(num_arr, use_time_optimised=True)

    if next_greater_num:
        print(f'Next Greater Number of {num} with same set of digits, is: {next_greater_num}')
    else:
        print('No Greater Number exists, with same set of digits')


if __name__ == '__main__':
    run()
