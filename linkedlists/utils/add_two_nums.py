# Problem Statement
# https://www.geeksforgeeks.org/sum-of-two-linked-lists/

from linkedlists import SinglyLinkedList, BuildSinglyLinkedList
from linkedlists.utils import reverse_linked_list
from stacks import LinkedStack


class GetLLSum:
    pass

def get_numbers_sum(num1: SinglyLinkedList, num2: SinglyLinkedList, use_recursion=False):
    def _validate_ll(ll: SinglyLinkedList):
        for elem in ll:
            if isinstance(elem.data, int) and elem.data >= 0:
                continue
            raise ValueError('Elems of the LL should be +ve numbers')

    _validate_ll(num1)
    _validate_ll(num2)

    ###########################################################################
    # Using Reverse LL
    # Time Complexity: O(M + N + M + M)
    # M = Length of longer LL
    # N = Length of smaller LL

    # Reversing of 2 LL = O(M + N)
    # Traversing both LL, to get summation of numbers = O(M)
    # Final traversing of summed LL, to print the digits in the summed number = O(M)
    def _get_numbers_sum():
        reverse_num1_head = reverse_linked_list(num1)
        reverse_num2_head = reverse_linked_list(num2)
        carry = 0

        numbers_sum = LinkedStack()
        while reverse_num1_head or reverse_num2_head:
            num1_digit = reverse_num1_head.data if reverse_num1_head is not None else 0
            num2_digit = reverse_num2_head.data if reverse_num2_head is not None else 0

            total_sum_of_digits = num1_digit + num2_digit + carry
            digit_in_final_sum = total_sum_of_digits % 10
            carry = total_sum_of_digits // 10

            numbers_sum.push(digit_in_final_sum)

            reverse_num1_head = reverse_num1_head.next if reverse_num1_head else None
            reverse_num2_head = reverse_num2_head.next if reverse_num2_head else None

        return numbers_sum
    ###########################################################################
    def _get_numbers_sum_using_recursion():
        num1_len = len(num1)
        num2_len = len(num2)

        if abs(num1_len - num2_len):



    exec_func = _get_numbers_sum_using_recursion if use_recursion else _get_numbers_sum
    return exec_func()


# driver code
def run():
    num1 = BuildSinglyLinkedList(list_of_nodes=[6, 4, 9, 5, 7, ]).get_ll()  # represents num = 64957
    num2 = BuildSinglyLinkedList(list_of_nodes=[4, 8, ]).get_ll()  # represents num = 48
    # summed_num = get_numbers_sum(num1, num2)
    summed_num = get_numbers_sum(num1, num2, use_recursion=True)

    print('Sum of given numbers is: ')
    summed_num.print_stack()


if __name__ == '__main__':
    run()