# Problem Statement
# https://www.geeksforgeeks.org/power-set/

from typing import Set

from mathematical.bit_manipulations.utils.get_set_bits_pos import get_set_bits_pos


def get_power_set(cet: Set):
    set_len = len(cet)
    list_from_set = list(cet)
    for num in range(2**set_len):
        c_num = num
        power_set_elem = ''


        print('num: ', num)
        for set_bit_pos in get_set_bits_pos(c_num):


            print('set_bit_pos: ', set_bit_pos)
            power_set_elem += list_from_set[set_bit_pos - 1]

        yield power_set_elem


# driver code
def run():
    cet = {'a', 'b', 'c', }
    for power_set_elem in get_power_set(cet):
        # print(power_set_elem)
        pass


if __name__ == '__main__':
    run()
