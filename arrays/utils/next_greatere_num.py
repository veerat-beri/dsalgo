# Problem Statement
# https://www.geeksforgeeks.org/find-next-greater-number-set-digits/


def get_next_greater_num(num: str):
    str_len = len(num)
    pivot_index = -1
    for str_index in range(str_len - 2, -1, -1):
        if num[str_index] < num[str_index + 1]:
            pivot_index = str_index
            break

    if pivot_index == -1:
        return


# driver code
def run():
    num = '218765'
    next_greater_num = get_next_greater_num(num)

    if next_greater_num:
        print(f'Next Greater Number of {num} with same set of digits, is: {next_greater_num}')
    else:
        print('No Greater Number exists, with same set of digits')


if __name__ == '__main__':
    run()
