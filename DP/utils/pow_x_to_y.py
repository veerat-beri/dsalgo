# Problem Statement
# https://www.geeksforgeeks.org/write-a-c-program-to-calculate-powxn/


# Recursive Approach
def power(x, y):
    if y == 0:
        return 1
    if y % 2 == 0:
        return power(x, y // 2) * power(x, y // 2)
    return x * power(x, y // 2) * power(x, y // 2)
##########################################################################################


# driver code
def run():
    x = 10
    y = 5
    ans = power(x, y)

    print(f'pow({x}, {y}) is: ', ans)


if __name__ == '__main__':
    run()

