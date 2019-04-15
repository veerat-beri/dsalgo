# Problem Statement
# https://www.geeksforgeeks.org/find-position-element-sorted-array-infinite-numbers/

from arrays import binary_search


def get_elem_index_in_infinite_stream(stream: [], num: int):
    k = 0
    end_index = 0

    while stream[end_index] < num:
        k += 1
        end_index = 1 << k

    return binary_search(stream, end_index >> 1, end_index, num)


# driver code
def run():
    stream = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170, ]
    num = 10
    num = 11
    # num = 3
    num_index = get_elem_index_in_infinite_stream(stream, num)

    if num_index is not None:
        print(f'Element({num}) found at index: {num_index}')
    else:
        print(f'Element({num}) not found')


if __name__ == '__main__':
    run()
