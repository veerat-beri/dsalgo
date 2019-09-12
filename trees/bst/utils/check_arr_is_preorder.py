# Problem Statement
# https://www.geeksforgeeks.org/check-if-a-given-array-can-represent-preorder-traversal-of-binary-search-tree/


def do_represent_pre_order(arr: []):
    # Naive O(N^2)
    arr_len = len(arr)
    if arr_len <= 1:
        return True

    first_elem = arr[0]
    first_greater_elem_index = 0

    for arr_index in range(1, arr_len):
        if arr[arr_index] >= first_elem:
            if not first_greater_elem_index:
                first_greater_elem_index = arr_index
        else:
            if first_greater_elem_index and arr_index > first_greater_elem_index:
                return False

    if first_greater_elem_index:
        return do_represent_pre_order(arr[:first_greater_elem_index]) and do_represent_pre_order(arr[first_greater_elem_index:])
    return do_represent_pre_order(arr[1:])


# driver code
def run():
    # preorder_arr = [2, 4, 3, ]
    # preorder_arr = [2, 4, 1, ]
    # preorder_arr = [40, 30, 35, 80, 100, ]
    preorder_arr = [40, 30, 35, 20, 80, 100, ]
    # preorder_arr = [8, 3, 1, 6, 4, 7, 10, 14, 13, ]
    print(f'Given Array: {preorder_arr}')
    is_preorder_arr = do_represent_pre_order(preorder_arr)
    print('Given array{}represents pre-order of a BST'.format(' ' if is_preorder_arr else ' do not '))


if __name__ == '__main__':
    run()
