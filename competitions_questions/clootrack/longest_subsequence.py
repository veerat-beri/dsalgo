# Problem Statement


#############################################################################################################
# SOLUTION
#############################################################################################################
def get_max_child(arr):
    sorted_arr = sorted(arr, reverse=True)
    index, global_max_count = 1, 1
    arr_len = len(sorted_arr)
    while index < arr_len:
        local_max_count = 1
        while index < arr_len and (sorted_arr[index] - sorted_arr[index - 1] in [0, -1]):
            local_max_count += 1
            index += 1

        global_max_count = max(local_max_count, global_max_count)
        index += 1

    return global_max_count


no_of_test_cases = int(input())
for test_case in range(no_of_test_cases):
    arr_size = int(input())
    arr = list(map(int, input().strip().split()))
    print(get_max_child(arr))

