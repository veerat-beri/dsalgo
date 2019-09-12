# Problem Statement
# https://www.geeksforgeeks.org/previous-greater-element/
from stacks import BuildLinkedStack


def get_previous_greater_elem(arr: []):
    intermediate_processing_stack = BuildLinkedStack().build()
    previous_greater_elem_stack = BuildLinkedStack().build()

    for arr_index in range(len(arr)):
        while not intermediate_processing_stack.is_empty() and arr[arr_index] > intermediate_processing_stack.top:
            intermediate_processing_stack.pop()
        if intermediate_processing_stack.is_empty():
            previous_greater_elem_stack.push(-1)
        else:
            previous_greater_elem_stack.push(intermediate_processing_stack.top)
        intermediate_processing_stack.push(arr[arr_index])

    return previous_greater_elem_stack


# driver code
def run():
    arr = [10, 4, 2, 20, 40, 12, 30, ]
    print(f'Given array: \n{arr}')
    print(f'Previous Greater elements in given array(in reverse order): \n{get_previous_greater_elem(arr)}')


if __name__ == '__main__':
    run()
