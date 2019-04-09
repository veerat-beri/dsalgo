# Problem Statement
# https://www.geeksforgeeks.org/find-excel-column-name-given-number/


def get_name_from_num(num: int):
    name_string = []

    def _get_char(num: int):
        return chr(ord('A') + num - 1)

    while num:
        rem = num % 26
        if not rem:
            name_string.append('Z')
            num = num // 26 - 1
        else:
            name_string.append(_get_char(rem))
            num = num // 26

    return ''.join(name_string[::-1])


# driver code
def run():
    # col_num = 702
    col_num = 26
    print(f'Column name for the column number {col_num} is: {get_name_from_num(col_num)}')


if __name__ == '__main__':
    run()
