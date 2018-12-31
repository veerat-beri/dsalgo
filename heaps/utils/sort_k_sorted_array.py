# Problem Statement
# https://www.geeksforgeeks.org/nearly-sorted-algorithm/


import heapq


def get_sorted_arr_from_k_sorted(arr: list, k):
    heap = arr[:k + 1]
    heapq.heapify(heap)
    yield heapq.heappop(heap)

    for index in range(k + 1, len(arr)):
        heapq.heappush(heap, arr[index])
        yield heapq.heappop(heap)

    while heap:
        yield heapq.heappop(heap)


# driver code
def run():
    arr = [6, 5, 3, 2, 8, 10, 9]
    k = 3
    print(f'Completely Sorted Array of {arr}: ')
    for elem in get_sorted_arr_from_k_sorted(arr, k):
        print(elem, end=' ')


if __name__ == '__main__':
    run()
