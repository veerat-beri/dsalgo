# Problem Statement
# https://www.geeksforgeeks.org/find-nth-magic-number/


from math import log2


def get_nth_magic_num(n: int)-> int:
    #############################################
    # 1st Approach
    # Time-complexity: O(num-of-set-bits * log2(n))
    #############################################
    # def _get_rightmost_set_bit_pos(n: int):
    #     return int(log2(n & -n))
    #
    # res = 0
    # while n:
    #     res += pow(5, _get_rightmost_set_bit_pos(n) + 1)
    #     n = n & n-1
    # return res
    #############################################
    # 2nd Approach
    # Time-complexity: O(num-of-bits)
    #############################################
    res = 0
    pow_of_5 = 1

    while n:
        pow_of_5 *= 5
        if n & 1:
            res += pow_of_5
        n >>= 1

    return res


# driver code
def run():
    n = 6
    print(f'N({n})th magic number is: {get_nth_magic_num(n)}')


if __name__ == '__main__':
    run()
