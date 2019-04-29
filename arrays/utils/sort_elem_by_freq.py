# Problem Statement
# https://www.geeksforgeeks.org/sort-elements-by-frequency/
# https://www.geeksforgeeks.org/sort-elements-frequency-set-4-efficient-approach-using-hash/


from collections import OrderedDict


# Efficient Approach using Ordered Dict/Linked HashMap
def get_sorted_arr_by_freq(arr: []):
    elem_count_dict = OrderedDict()
    sorted_arr = []

    for elem in arr:
        if elem_count_dict.get(elem):
            elem_count_dict[elem] += 1
            continue
        elem_count_dict[elem] = 1

    for elem in sorted(elem_count_dict, key=elem_count_dict.get, reverse=True):
        for _ in range(elem_count_dict[elem]):
            sorted_arr.append(elem)

    return sorted_arr


# driver code
def run():
    arr = [2, 5, 2, 8, 5, 6, 8, 8]
    sorted_arr = get_sorted_arr_by_freq(arr)
    print('Sorted sorted_arrays by frequency is: ', sorted_arr, sep='\n')


if __name__ == '__main__':
    run()
