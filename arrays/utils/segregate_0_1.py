# Problem Statement
# https://www.geeksforgeeks.org/segregate-0s-and-1s-in-an-array-by-traversing-array-once/


# Using 2 pointer Approach
# Time Complexity: O(N) (Single traversal)
# Space Complexity: O(1)
def get_sorted_binary_arr(binary_arr: []):
    arr_len = len(binary_arr)
    zeros_index = 0
    ones_index = arr_len - 1

    while zeros_index < ones_index:
        if binary_arr[zeros_index] == 1:
            binary_arr[zeros_index], binary_arr[ones_index] = binary_arr[ones_index], binary_arr[zeros_index]
            ones_index -= 1
        else:
            zeros_index += 1

    return binary_arr


# driver code
def run():
    binary_arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
    print(f'Initial array: {binary_arr}')
    print(f'Array after segregating 0s and 1s: {get_sorted_binary_arr(binary_arr)}')


if __name__ == '__main__':
    run()
