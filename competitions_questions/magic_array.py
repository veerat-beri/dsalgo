from math import sqrt, ceil

prime_nos = set()
not_prime_nos = set()
num_min_conversion_cost_map = {}
no_having_3_divisors = set()
no_not_having_3_divisors = set()


def _report_prime(num):
    prime_nos.add(num)
    return True


def _report_not_prime(num):
    not_prime_nos.add(num)
    return False


def is_prime(num) -> bool:
    if num in prime_nos:
        return True
    if num in not_prime_nos:
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


def is_having_3_divisors(num) -> bool:
    if num in no_having_3_divisors:
        return True
    if num in no_not_having_3_divisors:
        return False

    sqrt_of_num = sqrt(num)
    if sqrt_of_num.is_integer():
        if is_prime(sqrt_of_num):
            no_having_3_divisors.add(num)
            return True
    no_not_having_3_divisors.add(num)
    return False


def get_min_operations(arr, k):
    def _get_min_conversion_cost(num):
        if num_min_conversion_cost_map.get(num):
            return num_min_conversion_cost_map[num]

        if num == 1:
            return 3

        if is_having_3_divisors(num):
            num_min_conversion_cost_map[num] = 0
            return 0

        return -1

    def get_min_conversion_cost(num):

        num_conversion_cost = _get_min_conversion_cost(num)
        if num_conversion_cost != -1:
            num_min_conversion_cost_map[num] = num_conversion_cost
            return num_conversion_cost

        count = 0
        dup_num = num + 1
        while True:
            count += 1
            num_conversion_cost = _get_min_conversion_cost(dup_num)
            if num_conversion_cost == -1:
                dup_num += 1
                continue
            break
        one_count = count

        count = 0
        dup_num = num - 1
        while True:
            count += 1
            num_conversion_cost = _get_min_conversion_cost(dup_num)
            if num_conversion_cost == -1:
                dup_num -= 1
                continue
            break

        second_count = num_conversion_cost + count

        get_min_conversion_cost(num + 1)
        num_min_conversion_cost = min(one_count, second_count)
        num_min_conversion_cost_map[num] = num_min_conversion_cost

        return num_min_conversion_cost

    no_of_elem_to_be_deleted = len(arr) - k
    arr_elem_conversion_costs = []
    for elem in arr:
        arr_elem_conversion_costs.append(get_min_conversion_cost(elem))

    sorted_arr_elem_conversion_costs = sorted(arr_elem_conversion_costs, reverse=True)

    return sum(sorted_arr_elem_conversion_costs[no_of_elem_to_be_deleted:]) + no_of_elem_to_be_deleted


arr_size, k = list(map(int, input().strip().split()))
arr = list(map(int, input().strip().split()))  # 1 4 10 8 15
print(get_min_operations(arr, k))
