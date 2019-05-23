# Problem Statement
# https://www.geeksforgeeks.org/power-set/


def get_power_set(elem_list: []):
    set_len = len(elem_list)
    for num in range(2**set_len):
        power_set_elem = ''
        for nth_bit in range(set_len):
            # check if nth_bit is set in num
            if (1 << nth_bit) & num > 0:
                power_set_elem += elem_list[nth_bit]

        yield power_set_elem


# driver code
def run():
    elem_list = ['a', 'b', 'c', ]
    for power_set_elem in get_power_set(elem_list):
        print(power_set_elem)
        # pass


if __name__ == '__main__':
    run()
