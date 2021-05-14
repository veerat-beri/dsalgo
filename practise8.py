import math
import sys
from collections import Counter

max_num = pow(10, 6)
smallest_pf = [0 for _ in range(max_num + 1)]


def save_prime():
    smallest_pf[1] = 1
    for num in range(2, max_num + 1):
        smallest_pf[num] = num

    for num in range(4, max_num, 2):
        smallest_pf[num] = 2

    for i in range(3, math.ceil(math.sqrt(max_num))):
        if smallest_pf[i] == i:
            for j in range(i * i, max_num, i):
                if smallest_pf[j] == j:
                    smallest_pf[j] = i


def get_prime_factors(given_num):
    prime_factors_list = []
    while given_num != 1:
        prime_factors_list.append(smallest_pf[given_num])
        given_num = given_num // smallest_pf[given_num]

    return prime_factors_list


def get_all_comb(common_pfs, current_index=0, list_so_far=[]):
    if current_index == len(common_pfs):
        yield list_so_far
        return
    for l in get_all_comb(common_pfs, current_index + 1, list_so_far + [common_pfs[current_index], ]):
        yield l
    for l in get_all_comb(common_pfs, current_index + 1, list_so_far):
        yield l


def elevator_sol(X, Y, M):
    num1_pf = get_prime_factors(X)
    num2_pf = get_prime_factors(Y)

    common_pfs = list((Counter(num1_pf) & Counter(num2_pf)).elements())
    print(common_pfs)
    mul_set = set()
    for comb_list in get_all_comb(common_pfs):
        if comb_list:
            elem_prod = 1
            for elem in comb_list:
                elem_prod = elem_prod * elem

            mul_set.add(elem_prod)

    min_time = sys.maxsize
    floor = None

    print(mul_set)
    for elem in mul_set:
        num1 = X // elem
        num2 = Y // elem
        fac_len = len(get_prime_factors(num1)) + len(get_prime_factors(num2))
        if fac_len < min_time:
            min_time = fac_len
            floor = elem

    if floor:
        return min_time, floor
    return (-1, '')

    # mandatory_nums = []
    # for elem in common_pfs[::-1]:
    #     if elem >= M:
    #         mandatory_nums.append(elem)

    # prod = None
    # if mandatory_nums:
    #     prod = 1
    #     for elem in mandatory_nums:
    #         prod = prod*elem


save_prime()
# T = int(input())
for _ in range(1):
    # X, Y, M = map(int, input().split())
    X, Y, M = 20, 16, 10
    # X, Y, M = 100, 120, 10
    # X, Y, M = 160, 180, 10

    out_ = elevator_sol(X, Y, M)
    print(' '.join(map(str, out_)))
