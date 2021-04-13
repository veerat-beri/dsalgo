# Problem Statement
# https://www.geeksforgeeks.org/find-the-missing-number/
# https://leetcode.com/problems/missing-number/


class MissingNumber:
    def __init__(self, arr: []):
        self.arr = arr
        self.n = len(arr)

    # Time Complexity: O(2N)
    def get_missing_number(self):
        given_arr_xor = self.arr[0]

        for index in range(1, self.n):
            given_arr_xor ^= self.arr[index]

        actual_arr_xor = 1

        for elem in range(2, self.n + 2):
            actual_arr_xor ^= elem

        return given_arr_xor ^ actual_arr_xor


# driver code
def run():
    arr = [1, 2, 4, 5, 6]
    print(f'Missing number in {arr} is: {MissingNumber(arr).get_missing_number()}')


if __name__ == '__main__':
    run()
