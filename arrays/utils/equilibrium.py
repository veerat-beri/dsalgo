# Problem Statement
# https://www.geeksforgeeks.org/equilibrium-index-of-an-array/


# O(1) space and O(N) time solution
def find_equilibrium(arr):
    arr_sum = sum(arr)
    sum_when_traversing_from_left = 0
    for index in range(len(arr)):
        if arr_sum - sum_when_traversing_from_left - arr[index] == sum_when_traversing_from_left:
            return arr[index], index
        sum_when_traversing_from_left += arr[index]


def run():
    # arr = [10, 5, 3, 6, 1]
    arr = [-1, 2, -1, -1]

    equilibrium_point = find_equilibrium(arr)

    print(equilibrium_point)


if __name__ == '__main__':
    run()