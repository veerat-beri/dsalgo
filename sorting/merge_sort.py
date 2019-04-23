# Problem Statement
# https://www.geeksforgeeks.org/merge-sort/


def get_sorted_arr(arr: []):
    def _get_sorted_arr(low, high, ):
        if low > high:
            return

        mid = (high - low)//2 + low
        _get_sorted_arr(low, mid)
        _get_sorted_arr(mid + 1, high)



# driver code
def run():
    pass


if __name__ == '__main__':
    run()
