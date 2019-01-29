################################
# Problem Statement
# https://www.geeksforgeeks.org/binomial-coefficient-dp-9/


# Basic Implementation using 2-D array
def get_ncr(n, r, p=10**9 + 7, use_p=False):
    assert n >= 0 and r >= 0, 'n or r could not be -ve numbers'

    def _get_ncr_p(n, r):
        return (ncr[n - 1][r - 1] % p + ncr[n - 1][r] % p) % p

    def _get_ncr(n, r):
        return ncr[n - 1][r - 1] + ncr[n - 1][r]

    ncr = [[0 for _ in range(r + 1)] for _ in range(n + 1)]

    # Calculate value of Binomial Coefficient in bottom up manner
    for _n in range(n + 1):
        for _r in range(r + 1):
            if _n == 0 or _r == 0:
                ncr[_n][_r] = 1
            else:
                ncr[n][r] = ''

    return ncr[n][r]


# driver code
def run():
    n = 100
    r = 40
    print(f'nCr for given n={n} and r={r} is: {get_ncr(n, r)}')


if __name__ == '__main__':
    run()
