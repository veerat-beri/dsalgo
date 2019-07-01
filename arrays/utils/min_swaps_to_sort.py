# Problem Statement
# https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/


# Time-Complexity: O(N*logN + 2N)
# Space-Complexity: O(N)
def get_min_swaps_count(arr: []):
    enumerated_arr = list(enumerate(arr))
    # Sort as per ar-element
    sorted_enumerated_arr = sorted(enumerated_arr, key=lambda pair: pair[1])
    visited_elem_indexes = set()
    min_swaps_count = 0
    for elem_index in range(len(sorted_enumerated_arr)):
        if elem_index in visited_elem_indexes or sorted_enumerated_arr[elem_index][0] == elem_index:
            continue

        cycle_size = 0
        elem_index_dup = elem_index
        while elem_index_dup not in visited_elem_indexes:
            visited_elem_indexes.add(elem_index_dup)
            elem_index_dup = sorted_enumerated_arr[elem_index_dup][0]
            cycle_size += 1

        if cycle_size:
            min_swaps_count += cycle_size - 1

    return min_swaps_count


# driver code
def run():
    # arr = [4, 3, 2, 1, ]
    arr = [1, 5, 4, 3, 2, ]
    print(f'Given Array: {arr}')
    print(f'Sorted-Arr: {sorted(arr)}')
    print(f'minimum swaps required to sort the given array: {get_min_swaps_count(arr)}')


if __name__ == '__main__':
    run()
