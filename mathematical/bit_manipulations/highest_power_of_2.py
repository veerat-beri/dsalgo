# Problem Statement
# https://www.geeksforgeeks.org/highest-power-2-less-equal-given-number/


import sys


def get_max_power_of_2(num: int):
    # Method 1
    # dup_num = num
    # count = 0
    # while dup_num:
    #     dup_num = dup_num // 2
    #     count += 1
    # return count
    # Method 2
    ###############
    pass

def get_max_power_of_2(num: int):
    pass


# driver code
def run():
    num = sys.maxsize
    print(f'Max power of 2 in {num}: ', get_max_power_of_2(num), sep=' ')


if __name__ == '__main__':
    run()
