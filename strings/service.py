def get_relative_char(num: int, use_upper_case=False) -> chr:
    base_char_ascii_value = ord('A') if use_upper_case else ord('a')
    return chr(base_char_ascii_value + num - 1)


def get_relative_ascii(char, use_upper_case=False) -> int:
    base_char_ascii_value = ord('A') if use_upper_case else ord('a')
    return ord(char) - base_char_ascii_value
