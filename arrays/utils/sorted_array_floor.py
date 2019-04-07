# Problem Statement
# https://www.geeksforgeeks.org/floor-in-a-sorted-array/


def get_floor_index_in_sorted_array(arr: [], searched_num):
    arr_len = len(arr)

    def _get_floor_index_in_sorted_array(low, high):
        if low > high:
            return None

        if searched_num >= arr[high]:
            return high

        mid = (high - low)//2 + low

        if arr[mid] == searched_num:
            return mid

        ##############################
        # These two conditions are not just code-optimizing conditions, rather,
        # any one of them is necessary for correct output
        if searched_num < arr[mid] and mid > 0 and searched_num >= arr[mid - 1]:
            return mid - 1

        if searched_num > arr[mid] and mid < arr_len and searched_num <= arr[mid + 1]:
            return mid
        ##############################

        if arr[mid] < searched_num:
            return _get_floor_index_in_sorted_array(mid + 1, high)

        return _get_floor_index_in_sorted_array(low, mid - 1)

    return _get_floor_index_in_sorted_array(0, arr_len - 1)


# driver code
def run():
    arr = [1, 2, 4, 6, 10, 12, 14]
    searched_num = 7

    print(f'Floor of {searched_num} in given array is: ')
    floor_index = get_floor_index_in_sorted_array(arr, searched_num)
    if floor_index is not None:
        print(arr[floor_index])
    else:
        print('No floor exists!')


if __name__ == '__main__':
    run()
