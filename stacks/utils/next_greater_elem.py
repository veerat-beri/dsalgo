# Problem Statement
# https://www.geeksforgeeks.org/next-greater-element/


# Using Arr
from stacks import BuildLinkedStack


def get_next_greater_elem(arr: []):
    arr_len = len(arr)
    next_greater_elem_index_list = [None] * arr_len
    next_greater_elem_index_list[-1] = arr[-1]
    for arr_index in range(arr_len - 2, -1, -1):
        next_greater_elem_index_list[arr_index] = max(arr[arr_index], next_greater_elem_index_list[arr_index + 1])

    return next_greater_elem_index_list


# Using Stack
def get_next_greater_elem_using_stack(arr: []):
    next_greater_elem_stack = BuildLinkedStack().build()
    intermediate_processing_stack = BuildLinkedStack().build()
    # next_greater_elem_stack.push(-1)
    # max_elem_so_far = arr[-1]
    #
    # for arr_index in range(len(arr) - 1, -1, -1):
    #     if max_elem_so_far < arr[arr_index]:
    #         next_greater_elem_stack.push(-1)
    #     else:
    #         next_greater_elem_stack.push(max_elem_so_far)
    #     max_elem_so_far = max(arr[arr_index], max_elem_so_far)
    # in range(len(arr) - 1, -1, -1):
    for elem in arr[-1::-1]:
        while not intermediate_processing_stack.is_empty() and intermediate_processing_stack.top < elem:
            intermediate_processing_stack.pop()
        if intermediate_processing_stack.is_empty():
            next_greater_elem_stack.push(-1)
        else:
            next_greater_elem_stack.push(intermediate_processing_stack.pop())
        intermediate_processing_stack.push(elem)

    return next_greater_elem_stack

# # prints element and NGE pair for all
# # elements of arr[] of size n
# def printNGE(arr, n):
#     s = list()
#
#     arr1 = [0 for i in range(n)]
#
#     # iterating from n-1 to 0
#     for i in range(n-1, -1, -1):
#
#         # We will pop till we get the greater
#         # element on top or stack gets empty
#         while (len(s) > 0 and s[-1] < arr[i]):
#             s.pop() # if stack gots empty means there # is no element on right which is
#             # greater than the current element. #
#             # if not empty then the next greater # element is on top of stack
#         if (len(s) == 0):
#             arr1[i] = -1
#         else:
#             arr1[i] = s[-1]
#         s.append(arr[i])
#     for i in range(n):
#         print(arr[i], " ---> ", arr1[i] )


# driver code
def run():
    arr = [11, 13, 21, 3, ]
    # next_greater_elem_stack = get_next_greater_elem(arr)
    print(f'Given array: \n{arr}')
    print(f'Next Greater elements in given array: \n{get_next_greater_elem_using_stack(arr)}')
    # for elem in get_next_greater_elem_using_stack(arr):
    #     print(elem)


if __name__ == '__main__':
    run()
