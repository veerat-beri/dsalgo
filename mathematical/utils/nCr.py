################################################################################################
# Problem Statement
# https://www.geeksforgeeks.org/binomial-coefficient-dp-9/


# Basic Implementation using 2-D array
def get_ncr_basic(n, r, p=10**9 + 7, use_p=True):
    """
    Time-complexity = O(n*r)
    Space-complexity = O(n*r)
    """
    assert n >= 0 and r >= 0, 'n or r could not be -ve numbers'
    assert n >= r, 'n cann\'t be less than r'

    n_c_r = [[0 for _ in range(r + 1)] for _ in range(n + 1)]

    def _calc_ncr_with_p():
        for _n in range(n + 1):
            for _r in range(min(r, n) + 1):
                # base case
                if _r == 0 or _r == _n:  # nCr = 1 for nC0 and nCn
                    n_c_r[_n][_r] = 1
                else:
                    n_c_r[_n][_r] = (n_c_r[_n - 1][_r - 1] % p + n_c_r[_n - 1][_r] % p) % p

    def _calc_ncr():
        for _n in range(n + 1):
            for _r in range(min(r, n) + 1):
                # base case
                if _r == 0 or _r == _n:  # nCr = 1 for nC0 and nCn
                    n_c_r[_n][_r] = 1
                else:
                    n_c_r[_n][_r] = n_c_r[_n - 1][_r - 1] + n_c_r[_n - 1][_r]

    # Calculate value of Binomial Coefficient in bottom up manner
    _calc_ncr_with_p() if use_p else _calc_ncr()
    return n_c_r[n][r]


# Space Optimized version using 1-D array
def get_ncr_space_optimised(n, r, p=10**9 + 7, use_p=True):
    """
    Time-complexity = O(n*r)
    Space-complexity = O(r)
    :param n:
    :param r:
    :param p:
    :param use_p:
    :return:
    """
    assert n >= 0 and r >= 0, 'n or r could not be -ve numbers'
    assert n >= r, 'n cann\'t be less than r'

    ncr = [0 for _ in range(r + 1)]
    ncr[0] = 1

    def _calc_ncr_with_p():
        for _n in range(1, n + 1):
            _r = min(r, _n)
            while _r > 0:
                ncr[_r] = (ncr[_r] % p + ncr[_r - 1] % p) % p
                _r -= 1

    def _calc_ncr():
        for _n in range(1, n + 1):
            _r = min(r, _n)
            while _r > 0:
                ncr[_r] = ncr[_r] + ncr[_r - 1]
                _r -= 1

    # Calculate value of Binomial Coefficient in bottom up manner
    _calc_ncr_with_p() if use_p else _calc_ncr()
    return ncr[r]

################################################################################################
# Problem Statement
# https://www.geeksforgeeks.org/compute-ncr-p-set-2-lucas-theorem/

# Lucas Theorem
# def get_ncr(n, r, p=10**9 + 7, use_p=True):
#     pass
################################################################################################


# driver code
def run():
    n = 100
    r = 40
    print(f'nCr for given n={n} and r={r} is: {get_ncr_space_optimised(n, r)}')


if __name__ == '__main__':
    run()
