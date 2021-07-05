# Problem Statement
# https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/


def fibonacci_sequence():
    first_num, second_num = 0, 1

    yield first_num
    yield second_num

    while True:
        next_num = first_num + second_num
        yield next_num
        first_num, second_num = second_num, next_num


# driver code
def run():
    n = 10
    for fib_num in fibonacci_sequence():
        pass




if __name__ == '__main__':
    run()
