# Problem Statement
# https://www.geeksforgeeks.org/find-excel-column-name-given-number/


from strings.services import get_relative_char


def get_name_from_num(num: int):
    # MAX_NAME_STR_CHAR = 50
    # name_string = ['\0'] * MAX_NAME_STR_CHAR
    name_string = []
    # str_index = 0

    while num:
        rem = num % 26
        if not rem:
            # name_string[str_index] = 'Z'
            name_string.append('Z')
            num = num // 26 - 1
        else:
            # name_string[str_index] = _get_char(rem)
            name_string.append(get_relative_char(rem, use_upper_case=True))
            num = num // 26

        # str_index += 1

    return ''.join(name_string[::-1])


# driver code
def run():
    # col_num = 702
    col_num = 26
    print(f'Column name for the column number {col_num} is: {get_name_from_num(col_num)}')


if __name__ == '__main__':
    run()
