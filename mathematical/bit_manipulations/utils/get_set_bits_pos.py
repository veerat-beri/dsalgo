def get_set_bits_pos(num: int):
    def _get_set_bits_pos(num: int):
        while num:
            set_bit_pos = num & (-num)
            yield set_bit_pos
            num ^= set_bit_pos

    for set_bit_pos in _get_set_bits_pos(num):
        yield set_bit_pos
