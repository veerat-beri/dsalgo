# Problem Statement
# https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/


def get_gcd(num1, num2):
    # Method 1
    while num2:
        num1, num2 = num2 % num1, num1
    return num1
    #############################################
    # Method 2
    #############################################


# driver code
def run():
    num1 = 12
    num2 = 3
    print(f'Gcd of {num1} and {num2} is:', get_gcd(num1, num2))


if __name__ == '__main__':
    run()
