# Problem Statement
# https://www.geeksforgeeks.org/array-rotation/


from mathematical.school_problems import get_gcd


# Efficient Juggling Algorithm
# Time Complexity: O(N) OR O( gcd(n, d)*(n//d + 1) )
# Space Complexity: O(1)
def get_rotated_arr(arr: [], total_rotations: int):
    assert arr, 'Array could not be empty'

    arr_len = len(arr)
    for rotation_set_index in range(get_gcd(arr_len, total_rotations)):
        set_first_rotated_elem = arr[rotation_set_index]
        previous_rotated_index = rotation_set_index
        while 1:
            next_rotating_index = total_rotations + previous_rotated_index
            if next_rotating_index >= arr_len:
                next_rotating_index = next_rotating_index - arr_len
            if next_rotating_index == rotation_set_index:
                break

            arr[previous_rotated_index] = arr[next_rotating_index]
            previous_rotated_index = next_rotating_index

        arr[previous_rotated_index] = set_first_rotated_elem
    return arr


# driver code
def run():
    arr = [1, 2, 3, 4, 5, 6, 7]
    total_rotations = 2
    print(f'Given arr: {arr}')
    print(f'New arr after {total_rotations} rotations is:', get_rotated_arr(arr, total_rotations))


if __name__ == '__main__':
    run()
