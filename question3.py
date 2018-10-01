def find_pair(arr, sum):
    for index in range(len(arr)):
        elem = arr[index]
        hash_set = set()
        another_no_in_pair = sum - elem
        if another_no_in_pair > 0 and (another_no_in_pair in hash_set):
            print('Yes, pair exist:({}, {})'.format(elem, another_no_in_pair))
            return
        hash_set.add(another_no_in_pair)


find_pair([1, 5, 3, 8, 7, 15], 11)