# Problem Statement
# https://www.geeksforgeeks.org/count-set-bits-in-an-integer/


def get_set_bits_count(num: int) -> int:
    count = 0
    while num:
        num = num & (num - 1)
        count += 1
    return count


# driver code
def run():
    num = 3
    print(f'No of set bits in {num}:', get_set_bits_count(num))


if __name__ == '__main__':
    run()
