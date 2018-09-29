def binary_search(arr, start, end, key):
    if start > end:
        return -1

    mid = (start + end)//2
    if key == arr[mid]:
        return mid

    elif arr[mid] < key:
        return binary_search(arr, mid + 1, end, key)

    else:
        return binary_search(arr, start, mid - 1, key)


arr = [10, 20, 30, 40, 50, 60]
key = int(input('Enter element to search: '))
res = binary_search(arr, 0, len(arr), key)
if res == -1:
    print('{} not found'.format(key))

else:
    print('{} found at: '.format(key), res)
