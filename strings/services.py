def get_relative_char(num: int, use_upper_case=False) -> chr:
    base_char_ascii_value = ord('A') if use_upper_case else ord('a')
    return chr(base_char_ascii_value + num)


def get_relative_ascii(char, use_upper_case=False) -> int:
    base_char_ascii_value = ord('A') if use_upper_case else ord('a')
    return ord(char) - base_char_ascii_value


def swap_chars(string: str, swap_index_1: int, swap_index_2: int):
    smaller_index = swap_index_1 if swap_index_1 < swap_index_2 else swap_index_2
    larger_index = smaller_index ^ swap_index_1 ^ swap_index_2
    new_str = string

    if smaller_index != larger_index:
        new_str = string[:smaller_index] + string[larger_index] + \
                  string[smaller_index + 1: larger_index] + string[smaller_index] + string[larger_index + 1:]
    return new_str
