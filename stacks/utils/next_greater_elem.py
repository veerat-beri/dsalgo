# Problem Statement
# https://www.geeksforgeeks.org/next-greater-element-in-same-order-as-input/

from stacks import BuildLinkedStack


# Using Stack
def get_next_greater_elem(arr: []):
    next_greater_elem_stack = BuildLinkedStack().build()
    intermediate_processing_stack = BuildLinkedStack().build()
    for elem in arr[-1::-1]:
        while not intermediate_processing_stack.is_empty() and intermediate_processing_stack.top < elem:
            intermediate_processing_stack.pop()
        if intermediate_processing_stack.is_empty():
            next_greater_elem_stack.push(-1)
        else:
            next_greater_elem_stack.push(intermediate_processing_stack.top)
        intermediate_processing_stack.push(elem)

    return next_greater_elem_stack


# driver code
def run():
    arr = [11, 13, 21, 3, ]
    print(f'Given array: \n{arr}')
    print(f'Next Greater elements in given array: \n{get_next_greater_elem(arr)}')


if __name__ == '__main__':
    run()
