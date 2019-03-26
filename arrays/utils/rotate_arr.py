# Problem Statement
# https://www.geeksforgeeks.org/array-rotation/


# Efficient Juggling Algorithm
from mathematical.school_problems import get_gcd


def get_rotated_arr(arr: [], total_rotations: int):
    assert arr, 'Array could not be empty'

    arr_len = len(arr)
    for rotation_set_index in range(get_gcd(arr_len, total_rotations)):
        set_first_rotated_elem = arr[rotation_set_index]
        first_rotated_index = rotation_set_index
        while 1:
            next_index = total_rotations + first_rotated_index
            if next_index == arr_len:
                break
            arr[next_index] = arr[next_index + total_rotations]
        arr[next_index - 1] = set_first_rotated_elem
    return arr


# driver code
def run():
    arr = [1, 2, 3, 4, 5, 6, 7]
    total_rotations = 2
    print(f'Given arr: {arr}')
    print(f'New arr after {total_rotations} rotations is:', get_rotated_arr(arr, total_rotations))


if __name__ == '__main__':
    run()
