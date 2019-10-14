# Problem Statement
# https://www.geeksforgeeks.org/find-element-given-index-number-rotations/


# Time Complexity: O(no of rotations)
# Space Complexity: O(1)
def get_new_index_after_rotations(arr: [], rotations_arr: [], searched_index: int):
    assert searched_index in range(len(arr)), 'searched_index in not in arr range'

    for rotation_arr_index in range(len(rotations_arr) - 1, -1, -1):
        rotated_lower_index = rotations_arr[rotation_arr_index][0]
        rotated_higher_index = rotations_arr[rotation_arr_index][1]

        if searched_index >= rotated_lower_index and searched_index <= rotated_higher_index:
            if searched_index == rotated_lower_index:
                searched_index = rotated_higher_index
            else:
                searched_index -= 1

    return searched_index


# driver code
def run():
    arr = [1, 2, 3, 4, 5, ]
    rotations = [[0, 2, ], [0, 3, ]]
    searched_index = 1

    print(f'Given array: {arr}')
    print(f'Given rotations:', rotations)
    print(f'Elem at index({searched_index}) after rotations is:',
          arr[get_new_index_after_rotations(arr, rotations, searched_index)])


if __name__ == '__main__':
    run()
