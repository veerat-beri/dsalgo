# Problem Statement
# https://www.geeksforgeeks.org/count-triplets-with-sum-smaller-that-a-given-value/

from typing import List


class PairExists:
    def __init__(self, arr: List, max_triplet_sum: int):
        self.arr = arr
        self.max_triplet_sum = max_triplet_sum

    def check_triplet_exists(self, **kwargs):
        if kwargs.get('use_sorting'):
            return self._using_sorting()
        return self._using_hashing()

# driver code
def run():
    pass


if __name__ == '__main__':
    run()
