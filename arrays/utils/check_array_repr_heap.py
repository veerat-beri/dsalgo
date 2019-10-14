# Problem Statement
# https://www.geeksforgeeks.org/how-to-check-if-a-given-array-represents-a-binary-heap/

from heaps.heap import MaxBinaryHeap, MinBinaryHeap

# Fails for heap = [65, 91, ].
# As loop break could occur due to multiple reasons and we can not judge
# end "index" value is due to loop termination or break, in case arr is small as [65, 91, ]

# def do_arr_repr_heap(heap: [], heap_type='MAX'):
#     heap_len = len(heap)
#     index = 0
#     if heap_type == 'MAX':
#         for index in range(heap_len - heap_len//2):
#             try:
#                 if heap[index] >= heap[2*index + 1] and heap[index] >= heap[2*index + 2]:
#                     continue
#             except IndexError:
#                 pass
#             break
#     else:
#         for index in range(heap_len - heap_len//2):
#             try:
#                 if heap[index] <= heap[2*index + 1] and heap[index] <= heap[2*index + 2]:
#                     continue
#             except IndexError:
#                 pass
#             break
#
#     if index >= heap_len - heap_len//2 - 1:
#         return True
#     return False


# Time Complexity: O(N)
# Space Complexity: O(1) (not considering recursion stack or iteration queue space)
class CheckArrIsHeap:
    MAX = MaxBinaryHeap
    MIN = MinBinaryHeap

    ITERATIVE = 'iterative'
    RECURSIVE = 'recursive'

    def __init__(self, arr: [], heap_class=MAX, exec_method=ITERATIVE):
        self.heap = arr
        self.heap_len = len(arr)
        self.heap_class = heap_class
        self.exec_method = exec_method

    def __get_children(self, parent_index: int):
        left_child_index = self.heap_class.get_left_child_index(parent_index)
        right_child_index = self.heap_class.get_right_child_index(parent_index)

        left_child = self.heap[left_child_index]
        right_child = self.heap[right_child_index] if right_child_index < self.heap_len else None

        return left_child, right_child

    def __is_not_heap_node(self, parent, left_child, right_child):
        if self.heap_class == self.MAX:
            return parent < left_child or (right_child and parent < right_child)
        return parent > left_child or (right_child and parent > right_child)

    # Iterative Approach
    def __iterative(self, arr_index, last_internal_node):
        for index in range(arr_index, last_internal_node):
            parent = self.heap[index]
            left_child, right_child = self.__get_children(index)

            if self.__is_not_heap_node(parent, left_child, right_child):
                return False

        return True

    # Recursive Approach
    def __recursive(self, arr_index, last_internal_node):
        if arr_index >= last_internal_node:
            return True

        parent = self.heap[arr_index]
        left_child, right_child = self.__get_children(arr_index)

        if self.__is_not_heap_node(parent, left_child, right_child):
            return False

        return self.__recursive(arr_index + 1, last_internal_node)

    def do_arr_repr_heap(self):
        exec_func = self.__iterative if self.exec_method == self.ITERATIVE else self.__recursive
        return exec_func(0, self.heap_len // 2)


# driver code
def run():
    # heap = [90, 15, 10, 7, 12, 2]
    heap = [65, 91, ]
    print(f'Given arr: {heap}')

    if CheckArrIsHeap(heap, CheckArrIsHeap.MAX, CheckArrIsHeap.RECURSIVE).do_arr_repr_heap():
        print('Represents Heap')
    else:
        print('It does not represent Heap')


if __name__ == '__main__':
    run()
