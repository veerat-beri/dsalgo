def get_binary_repr(num: int):
    # return bin(num)
    return '{:b}'.format(num)


def is_odd(num: int):
    return num & 1


def is_even(num: int):
    return not is_odd(num)
