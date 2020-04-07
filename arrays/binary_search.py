# Problem Statement
# https://www.geeksforgeeks.org/binary-search/


def binary_search(arr, start, end, key):
    if start > end:
        return

    mid = (end - start)//2 + start

    if key == arr[mid]:
        return mid
    elif arr[mid] < key:
        return binary_search(arr, mid + 1, end, key)
    else:
        return binary_search(arr, start, mid - 1, key)


# driver code
def run():
    arr = [10, 20, 30, 40, 50, 60]
    key = 50
    res = binary_search(arr, 0, len(arr) - 1, key)
    if res is not None:
        print('{} found at: '.format(key), res)
    else:
        print('{} not found!'.format(key))


if __name__ == '__main__':
    run()
