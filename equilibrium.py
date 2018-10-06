# O(1) space and O(N) time solution

def find_equilibrium(arr):
    arr_sum = sum(arr)
    sum_when_traversing_from_left = 0
    for elem in arr:
        if arr_sum - sum_when_traversing_from_left - elem == sum_when_traversing_from_left:
            print('elem: ', elem)
            break
        sum_when_traversing_from_left += elem

    else:
        print(-1)

# arr = [10, 5, 3, 6, 1]
arr = [-1, 2, -1, -1]

find_equilibrium(arr)
