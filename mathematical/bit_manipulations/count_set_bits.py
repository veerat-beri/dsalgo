# Problem Statement
# https://www.geeksforgeeks.org/count-set-bits-in-an-integer/


def get_set_bits_count(num: int) -> int:
    # Method 1
    # Time complexity O(K), K= no. of set bits
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
    # Method 3
    # Time complexity O(1)
    # list of set bits in numbers in range-> [1, 16]
    set_bits_count_arr = [0, 1, 1, 2, ]

# driver code
def run():
    num = 64
    print(f'No of set bits in {num}:', get_set_bits_count(num))


if __name__ == '__main__':
    run()
