# Problem Statement
# https://www.geeksforgeeks.org/equilibrium-index-of-an-array/


# Time Complexity: O(N)
# Space Complexity: O(1)
def find_equilibrium(arr):
    arr_sum = sum(arr)
    sum_so_far = 0
    for index in range(len(arr)):
        elem = arr[index]
        if sum_so_far == arr_sum - sum_so_far - elem:
            return index + 1
        sum_so_far += elem


def run():
    arr = [10, 5, 3, 6, 1]
    # arr = [1, 2, 3, 4]
    # arr = [-1, 2, -1, -1]

    equilibrium_index = find_equilibrium(arr)
    if equilibrium_index:
        print(f'Equilibrium point in {arr} is: \n{arr[equilibrium_index]} at index {equilibrium_index}')
    else:
        print('No Equilibrium exists!')


if __name__ == '__main__':
    run()
