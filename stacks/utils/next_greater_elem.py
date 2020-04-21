# Problem Statement
# https://www.geeksforgeeks.org/next-greater-element-in-same-order-as-input/

from stacks import BuildLinkedStack
from stacks.utils.mixins import GreaterElementMixin


class NextGreaterElement(GreaterElementMixin):
    def get_ans_arr(self):
        return BuildLinkedStack().build()

    def get_arr_traversal(self):
        return self.arr[-1::-1]

    def get_next_greater_elem(self):
        return self._get_greater_elem()


# driver code
def run():
    arr = [11, 13, 21, 3, ]
    # arr = [10, 5, 8, 11, 3, ]
    print(f'Given array: \n{arr}')
    print(f'Next Greater elements in given array: \n{NextGreaterElement(arr).get_next_greater_elem()}')


if __name__ == '__main__':
    run()
