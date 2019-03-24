# Problem Statement
# https://www.geeksforgeeks.org/sort-elements-by-frequency/


from collections import OrderedDict


def get_sorted_arr_by_freq(arr: []):
    elem_count_dict = OrderedDict()
    for elem in arr:
        if elem_count_dict.get(elem):
            elem_count_dict[elem] += 1
            continue
        elem_count_dict[elem] = 1

    # return [[elem]*elem_count_dict[elem] for elem in sorted(elem_count_dict, key=elem_count_dict.get, reverse=True)]
    sorted_arr = []
    for elem in sorted(elem_count_dict, key=elem_count_dict.get, reverse=True):
        for _ in range(elem_count_dict[elem]):
            sorted_arr.append(elem)

    return sorted_arr


# driver code
def run():
    arr = [2, 5, 2, 8, 5, 6, 8, 8]
    sorted_arr = get_sorted_arr_by_freq(arr)
    print('Sorted arr by frequency is: ', sorted_arr, sep='\n')


if __name__ == '__main__':
    run()
