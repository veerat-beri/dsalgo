# Problem Statement
# https://www.geeksforgeeks.org/how-to-check-if-a-given-array-represents-a-binary-heap/


def do_arr_repr_heap(heap: [], heap_type='MAX'):
    heap_len = len(heap)
    index = 0
    if heap_type == 'MAX':
        for index in range(heap_len - heap_len//2):
            try:
                if heap[index] >= heap[2*index + 1] and heap[index] >= heap[2*index + 2]:
                    continue
            except IndexError:
                pass
            break
    else:
        for index in range(heap_len - heap_len//2):
            try:
                if heap[index] <= heap[2*index + 1] and heap[index] <= heap[2*index + 2]:
                    continue
            except IndexError:
                pass
            break

    if index >= heap_len - heap_len//2 - 1:
        return True
    return False


# driver code
def run():
    heap = [90, 15, 10, 7, 12, 2]
    print(f'Given arr: {heap}')
    if do_arr_repr_heap(heap):
        print('Represents Max Heap')
    else:
        print('It does not represent Max Heap')


if __name__ == '__main__':
    run()
