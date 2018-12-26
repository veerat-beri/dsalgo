# Problem Statement
# https://www.geeksforgeeks.org/floor-in-a-sorted-array/


def get_floor_index_in_sorted_array(arr: [], searched_num):
    def _get_floor_index_in_sorted_array(low, high):
        if low > high:
            return None

        if searched_num >= arr[high]:
            return high

        mid = (high - low)//2 + low

        if arr[mid] == searched_num:
            return mid

        if arr[mid] > searched_num:
            return _get_floor_index_in_sorted_array(mid + 1, high)

        return _get_floor_index_in_sorted_array(low, mid - 1)

    return _get_floor_index_in_sorted_array(0, len(arr) - 1)


# driver code
def run():
    arr = [1, 2, 4, 6, 10, 12, 14]
    searched_num = 7

    print(f'Floor of {searched_num} in given array is: ')
    print(arr[get_floor_index_in_sorted_array(arr, searched_num)])


if __name__ == '__main__':
    run()
