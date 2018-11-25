# Problem statement
# https://www.geeksforgeeks.org/find-subarray-with-given-sum/


######################################################
# WRONG APPROACH --

# # kadane Algorithm implementation
# def find_sub_array_with_given_sum(arr, req_sum):
#     max_sum_till_point = 0
#
#     for elem in arr:
#         max_sum_till_point += elem
#         if max_sum_till_point == req_sum:
#             print('Yes')
#             return True
#
#         elif max_sum_till_point > req_sum:
#             max_sum_till_point = elem
#
#     return False
#
#
# # driver code
# arr = [5, 1, 9, 2, 3]  # failing case.
# sum = 10
# sub_array_with_given_sum_exists = find_sub_array_with_given_sum(arr, sum)
#
# # Thus this approach will not work, have to do with sliding window approach.

############################################################

# Sliding window approach
def get_sub_array_with_given_sum(arr, given_sum):
    if not len(arr):
        return False

    start_of_sub_array = 0
    current_sum = arr[0]
    index = 1

    while index <= len(arr):
        while current_sum > given_sum and start_of_sub_array <= index:
            current_sum -= arr[start_of_sub_array]
            start_of_sub_array += 1

        if current_sum == given_sum:
            return True, (start_of_sub_array, index)

        current_sum += arr[index]
        index += 1

    return False


# driver code
def run():
    arr = [1, 4, 20, 3, 10, 5, ]
    given_sum = 33
    get_sub_array_with_given_sum(arr, given_sum)


if __name__ == '__main__':
    run()
