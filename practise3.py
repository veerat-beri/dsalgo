from arrays.services import create_matrix


def binary_search_count(arr, n, key):
    left = 0
    right = n

    mid = 0
    while (left < right):

        mid = (right + left) // 2

        # Check if key is present in array
        if (arr[mid] == key):

            # If duplicates are
            # present it returns
            # the position of last element
            while (mid + 1 < n and arr[mid + 1] == key):
                mid += 1
            break


        # If key is smaller,
        # ignore right half
        elif (arr[mid] > key):
            right = mid

        # If key is greater,
        # ignore left half
        else:
            left = mid + 1

    # If key is not found in
    # array then it will be
    # before mid
    while (mid > -1 and arr[mid] > key):
        mid -= 1

    # Return mid + 1 because
    # of 0-based indexing
    # of array
    return mid + 1


def get_no_of_options(a: [], b: [], c: [], d: [], price: int):
    a.sort()
    b.sort()
    c.sort()
    d.sort()

    a_single, b_single, c_single, d_single = (False, False, False, False, )
    a_len = len(a)
    b_len = len(b)
    c_len = len(c)
    d_len = len(d)

    # if a_len == 1:
    #     price -= a[0]
    #     a_single = True
    #
    # if b_len == 1:
    #     price -= b[0]
    #     b_single = True
    #
    # if c_len == 1:
    #     price -= c[0]
    #     c_single = True
    #
    # if d_len == 1:
    #     price -= d[0]
    #     d_single = True
    #
    #
    # if a_single and b_single and c_single and d_single and price >=0 :
    #     return 1

    total_combinations = 0
    # b_index = b_len - 1
    # c_index = c_len - 1

    for elem_a in a:
        # print("elem a", elem_a)
        for elem_b in b[::-1]:
            # if price - elem_a - c[0] <= 0:
            #     continue

            # print("elem b", elem_b)
            for elem_c in c:
                # print("elem c", elem_c)
                diff = price - elem_a - elem_b - elem_c
                print("diff: ", diff)
                if diff > 0:
                    total_combinations += binary_search_count(d, d_len, diff)
                    break

    # print("here")
    return total_combinations


print(get_no_of_options([3, 2], [4, ], [2, 3, ], [1, 2, 3], 10))





