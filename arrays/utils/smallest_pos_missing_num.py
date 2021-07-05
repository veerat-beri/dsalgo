# Problem Statement
# https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/


def segregate_arr(arr):
    neg_index = 0
    pos_index = 0

    while pos_index < len(arr):
        if arr[pos_index] <= 0:
            arr[pos_index], arr[neg_index] = arr[neg_index], arr[pos_index]
            neg_index += 1
        pos_index += 1

    return neg_index


def reflect_occurrence(positive_arr):
    arr_size = len(positive_arr)
    for elem in positive_arr:
        if abs(elem) - 1 >= arr_size:
            continue

        positive_arr[abs(elem) - 1] = -positive_arr[abs(elem) - 1]


def get_min_positive(arr: []):
    print("Given array: ", arr)
    first_pos_index = segregate_arr(arr)
    print("array after segregation: ", arr)
    positive_arr = arr[first_pos_index:]
    print("positive arr:", positive_arr)

    reflect_occurrence(positive_arr)
    print("after processing array: ", positive_arr)

    positive_arr_len = len(positive_arr)
    for arr_index in range(positive_arr_len):
        if positive_arr[arr_index] > 0:
            return arr_index + 1

    return positive_arr_len + 1


# driver code
def run():
    arr = [-1, -2, 2, 0, 1, -3, 3, 4]
    # arr = [-1, -2, -4, 0, 1, -3, 3, 4]
    print("min positive number: ", get_min_positive(arr))


if __name__ == '__main__':
    run()
