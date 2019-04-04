# Problem Statement
# https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/


# Time Complexity: O(N) (Single Traversal)
# Space Complexity: O(1)
# Using 3 pointers
def get_sorted_arr_set_0_1_2(arr: []):
    arr_len = len(arr)
    zeros_index = 0
    ones_index = 0
    twos_index = arr_len - 1
    while ones_index < twos_index:
        if arr[ones_index] == 0:
            arr[zeros_index], arr[ones_index] = arr[ones_index], arr[zeros_index]
            zeros_index += 1
            ones_index += 1
        elif arr[zeros_index] == 2:
            arr[zeros_index], arr[twos_index] = arr[twos_index], arr[zeros_index]
            twos_index -= 1
        else:
            ones_index += 1
    return arr


# driver code
def run():
    arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    print(f'Given array: {arr}')
    print(f'array after sorting is: {get_sorted_arr_set_0_1_2(arr)}')


if __name__ == '__main__':
    run()
