# Problem Statement
# https://www.geeksforgeeks.org/sum-of-two-linked-lists/

from linkedlists import SinglyLinkedList, BuildSinglyLinkedList
from linkedlists.utils import reverse_linked_list
from stacks import LinkedStack


class _LLSumCalcUtils:
    def __init__(self, num1: SinglyLinkedList, num2: SinglyLinkedList):
        self.num1 = num1
        self.num2 = num2

        self.summed_num = LinkedStack()
        self._validate_ll(num1)
        self._validate_ll(num2)

    def _validate_ll(self, ll: SinglyLinkedList):
        for elem in ll:
            if isinstance(elem.data, int) and elem.data >= 0:
                continue
            raise ValueError('Elems of the LL should be +ve numbers')

    def _get_summed_num_with_carry(self, num1: int, num2: int, previous_carry: int = 0) -> (int, int):
        """
        :return: digit in summed-num, carry  # i.e if 9 + 1, then returns (0, 1)
        """
        total_sum_of_digits = num1 + num2 + previous_carry
        return total_sum_of_digits % 10, total_sum_of_digits // 10


class _GetLLSumUsingLLReversal(_LLSumCalcUtils):
    def compute_summed_ll(self):
        """
        Using Reverse LL

        Time Complexity: O(M + N + M + M)
        M = Length of longer LL
        N = Length of smaller LL

        Complexity Explanation:
        Reversing of 2 LL = O(M + N)
        Traversing both LL, to get summation of numbers = O(M)
        Final traversing of summed LL, to print the digits in the summed number = O(M)
        """
        reverse_num1_head = reverse_linked_list(self.num1)
        reverse_num2_head = reverse_linked_list(self.num2)
        carry = 0

        while reverse_num1_head or reverse_num2_head:
            num1_digit = reverse_num1_head.data if reverse_num1_head is not None else 0
            num2_digit = reverse_num2_head.data if reverse_num2_head is not None else 0

            digit_in_final_sum, carry = self._get_summed_num_with_carry(num1_digit, num2_digit, carry)

            self.summed_num.push(digit_in_final_sum)

            reverse_num1_head = reverse_num1_head.next if reverse_num1_head else None
            reverse_num2_head = reverse_num2_head.next if reverse_num2_head else None

        self.summed_num.push(carry)


class _GetLLSumUsingRecursionMixin(_LLSumCalcUtils):
    def _compute(self, num1_node, num2_node):
        if num1_node is None and num2_node is None:
            return 0

        previous_carry = self._compute(num1_node.next, num2_node.next)
        digit_in_final_sum, new_carry = self._get_summed_num_with_carry(num1_node.data, num2_node.data, previous_carry)
        self.summed_num.push(digit_in_final_sum)
        return new_carry

    def compute_equal_ll_sum_using_recursion(self, num1_current_node = None, num2_current_node = None):
        previous_carry = self._compute(num1_current_node or self.num1.head, num2_current_node or self.num2.head)
        if previous_carry:
            self.summed_num.push(previous_carry)

    def compute_unequal_ll_sum_using_recursion(self, larger_ll_current_node,
                                               smaller_ll_current_node,
                                               current_pos: int, len_diff: int):
        if current_pos == len_diff:
            return self._compute(larger_ll_current_node, smaller_ll_current_node)

        previous_carry = self.compute_unequal_ll_sum_using_recursion(larger_ll_current_node.next, smaller_ll_current_node, current_pos + 1, len_diff)
        digit_in_final_sum, new_carry = self._get_summed_num_with_carry(previous_carry, larger_ll_current_node.data)
        self.summed_num.push(digit_in_final_sum)
        return new_carry

    def compute_summed_ll(self):
        num1_len = len(self.num1)
        num2_len = len(self.num2)

        if num1_len == num2_len:
            self.compute_equal_ll_sum_using_recursion()

        elif num1_len > num2_len:
            self.compute_unequal_ll_sum_using_recursion(self.num1, self.num2, 0, num1_len - num2_len)

        else:
            self.compute_unequal_ll_sum_using_recursion(self.num2, self.num1, 0, num2_len - num1_len)

        return self.summed_num


class GetLLSum(_GetLLSumUsingLLReversal, _GetLLSumUsingRecursionMixin):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def get_numbers_sum(self, use_recursion=False):
        exec_class = _GetLLSumUsingRecursionMixin(num) if use_recursion else _GetLLSumUsingLLReversal()
        exec_class.compute_summed_ll()
        return self.summed_num


# driver code
def run():
    # num1 = BuildSinglyLinkedList(list_of_nodes=[6, 4, 9, 5, 7, ]).get_ll()  # represents num = 64957
    # num2 = BuildSinglyLinkedList(list_of_nodes=[4, 8, ]).get_ll()  # represents num = 48
    num1 = BuildSinglyLinkedList(list_of_nodes=[5, 6, 3, ]).get_ll()  # represents num = 563
    num2 = BuildSinglyLinkedList(list_of_nodes=[8, 4, 2, ]).get_ll()  # represents num = 842
    print('Given numbers to be summed are: ')
    print('num1: ')
    num1.print_linked_list()
    print('num2: ')
    num2.print_linked_list()

    # summed_num = GetLLSum(num1, num2).get_numbers_sum(use_recursion=True)
    summed_num = GetLLSum(num1, num2).get_numbers_sum()

    print('Sum of given numbers is: ')
    summed_num.print_stack()


if __name__ == '__main__':
    run()
