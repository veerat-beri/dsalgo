# Problem Statement
# https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/


# Time Complexity: O(N) (Single Traversal)
# Space Complexity: O(1)
# Using Dutch National Flag Algorithm, or 3-way Partitioning
# other ref: http://users.monash.edu/~lloyd/tildeAlgDS/Sort/Flag/
def segregate_0_1_2(arr: []):
    arr_len = len(arr)
    zeros_index = 0
    ones_index = 0
    twos_index = arr_len - 1
    while ones_index <= twos_index:
        # "<=" is required instead of obvious "<", as both zeros_index and twos_index
        # are advanced 1 extra, each time and their (zeros_index/twos_index) last element will get
        # skipped from checking, if "<" is used

        if arr[ones_index] == 0:
            arr[zeros_index], arr[ones_index] = arr[ones_index], arr[zeros_index]
            zeros_index += 1
            ones_index += 1
        elif arr[ones_index] == 2:
            arr[ones_index], arr[twos_index] = arr[twos_index], arr[ones_index]
            twos_index -= 1
        else:
            ones_index += 1
    return arr


# driver code
def run():
    arr = [0, 1, 1, 0, 1, 2, 1, 2, 2, 0, 0, 1]
    print(f'Given array: \n{arr}')
    segregate_0_1_2(arr)
    print(f'\nArray after segregating 0s, 1s and 2s: \n{arr}')


if __name__ == '__main__':
    run()
