# Problem Statement
# https://www.geeksforgeeks.org/program-to-find-lcm-of-two-numbers/


from mathematical.school_problems import get_gcd


def get_lcm(num1: int, num2: int):
    return (num1 * num2) / get_gcd(num1, num2)


# driver code
def run():
    num1, num2 = 12, 4
    print(f'LCM of {num1} and {num2} is: {get_lcm(num1, num2)}')


if __name__ == '__main__':
    run()
