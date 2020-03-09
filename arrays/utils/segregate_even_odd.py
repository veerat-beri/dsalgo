# Problem Statement
# https://www.geeksforgeeks.org/segregate-even-and-odd-numbers/

from mathematical.bit_manipulations.services import is_odd


# Using 2-way partitioning
# Time Complexity: O(N) (Single traversal)
# Space Complexity: O(1)
# other ref: http://users.monash.edu/~lloyd/tildeAlgDS/Sort/Flag/
def segregated_even_odd(arr: []):
    arr_len = len(arr)
    even_index = 0
    odd_index = arr_len - 1

    while even_index < odd_index:
        if is_odd(arr[even_index]):
            arr[even_index], arr[odd_index] = arr[odd_index], arr[even_index]
            odd_index -= 1
        else:
            even_index += 1


# driver code
def run():
    arr = [12, 34, 45, 9, 8, 90, 3]
    print(f'Initial array: \n{arr}')
    segregated_even_odd(arr)
    print(f'\nArray after segregating odds and evens: \n{arr}')


if __name__ == '__main__':
    run()
