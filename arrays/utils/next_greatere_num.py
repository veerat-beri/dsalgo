# Problem Statement
# https://www.geeksforgeeks.org/find-next-greater-number-set-digits/


from arrays.services import swap_arr_elem


def get_next_greater_num(num: []):
    num_len = len(num)

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

        swapping_index = pivot_index + 1
        next_greater_digit = num[swapping_index]

        for arr_index in range(pivot_index + 2, num_len):
            if num[arr_index] < next_greater_digit:
                next_greater_digit = num[arr_index]
                swapping_index = arr_index

        return pivot_index, swapping_index

    # Time complexity: O(N * log2 N + N)
    # Space Complexity: O(N)
    def _get_swapping_indexes_TO():
        pivot_index = -1
        min_so_far_list = []
        for arr_index in range(num_len - 2, -1, -1):
            if num[arr_index] < num[arr_index + 1]:
                pivot_index = arr_index
                break

        if pivot_index == -1:
            return None, None

        swapping_index = pivot_index + 1
        next_greater_digit = num[swapping_index]

        for arr_index in range(pivot_index + 2, num_len):
            if num[arr_index] < next_greater_digit:
                next_greater_digit = num[arr_index]
                swapping_index = arr_index

        return pivot_index, swapping_index

    pivot_index, swapping_index = _get_swapping_indexes()

    if pivot_index is None:
        return

    swap_arr_elem(pivot_index, swapping_index, num)
    num[pivot_index + 1:] = sorted(num[pivot_index + 1:])

    return ''.join(list(map(str, num)))


# driver code
def run():
    num = '218765'
    num = '28765'
    num = '321'
    num_arr = list(map(int, num))
    next_greater_num = get_next_greater_num(num_arr)

    if next_greater_num:
        print(f'Next Greater Number of {num} with same set of digits, is: {next_greater_num}')
    else:
        print('No Greater Number exists, with same set of digits')


if __name__ == '__main__':
    run()
