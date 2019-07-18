# Problem Statement
# https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/

from strings.services import swap_chars


class StringPermutations:
    def __init__(self, string: str):
        self.str_len = len(string)
        self.string = string

    def handle_permuted_str(self, permuted_string: str):
        print(permuted_string)

    # Time Complexity: O(N * N!)
    # This will give duplicate results for strings having repeated characters.
    def _get_all_permutations_with_duplicates(self, str_so_far: str, fixed_index: int):
        if fixed_index == self.str_len - 1:
            self.handle_permuted_str(str_so_far)
            return

        for str_index in range(fixed_index, self.str_len):
            swapped_str = swap_chars(str_so_far, fixed_index, str_index)
            self._get_all_permutations_with_duplicates(swapped_str, fixed_index + 1)

    def _get_all_permutations_without_duplicates(self):
        #############################################
        # Method 1, using set
        # Time Complexity: O(N * N! + N), here "+ N" is for final result set traversal
        # Space Complexity: O(N + log N), here log N is Stack-space
        unique_permutations = set()
        self.handle_permuted_str = lambda permuted_string: unique_permutations.add(permuted_string)
        self._get_all_permutations_with_duplicates(self.string, 0)

        for permuted_str in unique_permutations:
            print(permuted_str)
        #############################################

    def get_all_permutations(self):
        # self._get_all_permutations_with_duplicates(self.string, 0)
        self._get_all_permutations_without_duplicates()


# driver code
def run():
    string = 'abcc'
    print(f'All permutations of the string={string} are: \n')
    StringPermutations(string).get_all_permutations()


if __name__ == '__main__':
    run()
