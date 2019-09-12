# Problem Statement
# https://www.geeksforgeeks.org/sieve-of-eratosthenes/


# Sieve of Eratosthenes
# Time Complexity:
# Space Complexity: O(N)
def get_all_primes(upper_limit_num: int) -> list:
    assert upper_limit_num >= 0, '-ve nos are not allowed, try with their absolute values!'

    is_prime = [True] * (upper_limit_num + 1)

    num = 2
    while num * num <= upper_limit_num:
        if is_prime[num]:
            for tmp_num in range(num*num, upper_limit_num + 1, num):
                is_prime[tmp_num] = False
        num += 1

    # mark 0 and 1 as not-prime
    for index in range(2 if upper_limit_num >= 1 else 1):
        is_prime[index] = False

    return is_prime


# driver code
def run():
    upper_limit_num = 10000
    all_nums = get_all_primes(upper_limit_num)
    print(f'All prime numbers till "{upper_limit_num}" are: ')
    print([index for index in range(upper_limit_num + 1) if all_nums[index]])


if __name__ == '__main__':
    run()
