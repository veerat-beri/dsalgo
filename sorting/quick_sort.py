def get_pivot_index(arr, lower_index, higher_index, partitioning_elem: int = None, use_randomise=True):
    pivot_index = 0

    assert not (use_randomise and partitioning_elem), 'can not perform random partition on provided element'

    if partitioning_elem:
        try:
            partitioning_elem_index = arr.index(partitioning_elem)
            arr[higher_index], arr[partitioning_elem_index] = arr[partitioning_elem_index], arr[higher_index]
        except:
            print('Given Partition element is not in array')

    partitioning_elem = arr[higher_index]

    for index in range(lower_index, higher_index):
        if arr[index] < partitioning_elem:
            arr[index], arr[pivot_index] = arr[pivot_index], arr[index]
            pivot_index += 1

    arr[higher_index], arr[pivot_index] = arr[pivot_index], arr[higher_index]
    return pivot_index


# driver code
def run():
    arr = [12, 3, 5, 7, 11, 2, ]
    print(f'Partition index in given array is: {get_pivot_index(arr, 0, len(arr) - 1)}')
    print(f'Array after partitioning: {arr}')


if __name__ == '__main__':
    run()
