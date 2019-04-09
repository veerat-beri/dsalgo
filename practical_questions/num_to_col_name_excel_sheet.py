# Problem Statement
# https://www.geeksforgeeks.org/find-excel-column-name-given-number/


def get_name_from_num(num: int):
    MAX_NAME_STR_CHAR = 50
    name_string = ['\0'] * MAX_NAME_STR_CHAR
    str_index = 0

    def _get_char(num: int):
        return chr(ord('A') + num - 1)

    while num:
        rem = num % 26
        if not rem:
            name_string[str_index] = 'Z'
            num = num // 26 - 1
        else:
            name_string[str_index] = _get_char(rem)
            num = num // 26

        str_index += 1



    print(name_string)
    return name_string


# driver code
def run():
    col_num = 702
    print(f'Column name for the column number {col_num} is: {get_name_from_num(col_num)}')


if __name__ == '__main__':
    run()
