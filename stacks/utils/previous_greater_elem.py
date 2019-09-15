# Problem Statement
# https://www.geeksforgeeks.org/previous-greater-element/

from queues.build_queue import BuildLinkedQueue
from stacks.utils.mixins import GreaterElementMixin


class PreviousGreaterElement(GreaterElementMixin):
    def get_ans_arr(self):
        return BuildLinkedQueue().build()

    def get_arr_traversal(self):
        return self.arr

    def get_previous_greater_elem(self):
        return self._get_greater_elem()


# driver code
def run():
    arr = [10, 4, 2, 20, 40, 12, 30, ]
    print(f'Given array: \n{arr}')
    print(f'Previous Greater elements in given array: \n{PreviousGreaterElement(arr).get_previous_greater_elem()}')


if __name__ == '__main__':
    run()
