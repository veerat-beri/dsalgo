# Problem Statement
# https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/


def get_lis_length(arr: []):
    def _get_lis_length(untraversed_arr_len):
        if untraversed_arr_len == 1:
            return 1

        max_lis_till_arr_index = 1
        for arr_index in range(1, untraversed_arr_len):
            lis_till_arr_index = _get_lis_length(arr_index)
            if arr[arr_index - 1] < arr[untraversed_arr_len - 1] and lis_till_arr_index + 1 > max_lis_till_arr_index:
                max_lis_till_arr_index = lis_till_arr_index + 1

        return max_lis_till_arr_index

    return _get_lis_length(len(arr))


def run():
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80, ]
    print(f'Max LIS length in given array: {get_lis_length(arr)}')


if __name__ == '__main__':
    run()
