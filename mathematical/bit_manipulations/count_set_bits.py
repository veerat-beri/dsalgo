# Problem Statement
# https://www.geeksforgeeks.org/count-set-bits-in-an-integer/


import sys


def get_set_bits_count(num: int) -> int:
    # Method 1 -> Time complexity O(K), K= no. of set bits
    # Brian Kernighan’s Algorithm
    ###############
    # count = 0
    # while num:
    #     num = num & (num - 1)
    #     count += 1
    # return count
    ###############
    # Method 2
    # return bin(num).count('1')
    ###############
    # Method 3 -> Time complexity O(log(n, 16)) ~ O(1)

    # list of set bits in numbers in range-> [1, 16]
    set_bits_count_arr = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]

    def _get_set_bits_count(num: int):
        if num == 0:
            return set_bits_count_arr[0]

        num_last_nibble = num & 0xf  # nibble = 4-bits
        return set_bits_count_arr[num_last_nibble] + _get_set_bits_count(num >> 4)
    return _get_set_bits_count(num)


# driver code
def run():
    num = sys.maxsize
    print(f'No of set bits in {num}:', get_set_bits_count(num))


if __name__ == '__main__':
    run()
