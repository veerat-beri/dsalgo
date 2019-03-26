# Problem Statement
# https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/


def get_gcd(num1, num2):
    # Method 1 (Iterative)
    # while num1:
    #     num1, num2 = num2 % num1, num1
    # return num2
    #############################################
    # Method 2 (Recursive)
    def _get_gcd(num1, num2):
        if num1 == 0:
            return num2
        return _get_gcd(num2 % num1, num1)
    return _get_gcd(num1, num2)
    #############################################


# driver code
def run():
    num1 = 12
    num2 = 3
    print(f'Gcd of {num1} and {num2} is:', get_gcd(num1, num2))


if __name__ == '__main__':
    run()
