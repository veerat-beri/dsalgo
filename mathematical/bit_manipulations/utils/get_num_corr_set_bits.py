# Problem Statement
#


def get_set_bits_num(num: int):
    def _get_set_bits_num(num: int):
        while num:
            set_bit_pos = num & (-num)
            yield set_bit_pos
            num ^= set_bit_pos

    for set_bit_pos in _get_set_bits_num(num):
        yield set_bit_pos


def run():
    num = 109
    print(f'Numbers corresponding to set-bits in {num} are: ')
    for set_bit_pos in get_set_bits_num(num):
        print(set_bit_pos)


if __name__ == '__main__':
    run()
