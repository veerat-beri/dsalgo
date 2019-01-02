# Problem Statement
# https://www.geeksforgeeks.org/primality-test-set-1-introduction-and-school-method/


def get_is_prime(num) -> bool:
    def _report_prime(num):
        # Could be overridden to perform some other additional tasks
        return True

    def _report_not_prime(num):
        # Could be overridden to perform some other additional tasks
        return False

    # Corner cases
    if num <= 1:
        return _report_not_prime(num)
    if num <= 3:
        return _report_prime(num)

    # This is checked so that we can skip
    # middle five numbers in below loop
    if num % 2 == 0 or num % 3 == 0:
        return _report_not_prime(num)

    start_index = 5
    while start_index * start_index <= num:
        if num % start_index == 0 or num % (start_index + 2) == 0:
            return _report_not_prime(num)
        start_index = start_index + 6

    return _report_prime(num)


def run():
    num = 101
    print(f'Gievn No: {num}')
    if get_is_prime(num):
        print('No is Prime No.')
    else:
        print('No is not a Prime No.')


if __name__ == '__main__':
    run()