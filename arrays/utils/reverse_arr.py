# Problem Statement
# https://leetcode.com/problems/reverse-string/description/

######################################
# Iterative approach
# In place reversal

def reverse_arr_iterative(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

######################################
# Recursive Approach
# In place reversal


def reverse_arr_recursive(input_arr, right, left=0):
    if left >= right:
        return
    input_arr[left], input_arr[right] = input_arr[right], input_arr[left]
    reverse_arr_recursive(input_arr, right - 1, left + 1)


# driver code
def run():
    input_arr = ["h", "e", "l", "l", "o"]
    print('Given arr: ', input_arr)

    reverse_arr_iterative(input_arr)
    print('\nUsing iterative approach, arr reverse: ', input_arr)

    # Need to redeclare as earlier method changed original arr due to inplace reversal
    input_arr = ["h", "e", "l", "l", "o"]

    reverse_arr_recursive(input_arr, len(input_arr) - 1)
    print('Using recursive approach, arr reverse: ', input_arr)


if __name__ == '__main__':
    run()
