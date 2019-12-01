# Problem Statement
# https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/

from strings.services import swap_chars


class StringPermutations:
    def __init__(self, string: str):
        self.str_len = len(string)
        self.string = string

    # Time Complexity: O(N * N!)
    # This will give duplicate results for strings having repeated characters.
    def _get_all_permutations_with_duplicates(self, str_so_far: str, fixed_index: int = 0):
        if fixed_index == self.str_len - 1:
            yield str_so_far
            return

        for str_index in range(fixed_index, self.str_len):
            if fixed_index != str_index and str_so_far[str_index] == str_so_far[fixed_index]:
                continue
            swapped_str = swap_chars(str_so_far, fixed_index, str_index)
            for string in self._get_all_permutations_with_duplicates(swapped_str, fixed_index + 1):
                yield string

    def _get_all_permutations_without_duplicates(self, *args):
        #############################################
        # Method 1, using set
        # Time Complexity: O(N * N!)
        # Space Complexity: O(N + log N), here log N is Stack-space
        unique_permutations = set()

        for string in self._get_all_permutations_with_duplicates(self.string):
            if string in unique_permutations:
                continue
            unique_permutations.add(string)
            yield string
        #############################################

    def print_all_permutations(self):
        count = 1
        for string in self._get_all_permutations_without_duplicates(self.string):
            print(count, string)
            count += 1


# Problem Statement
# https://www.geeksforgeeks.org/generate-all-the-binary-strings-of-n-bits/
class StringOfNBits:
    def __init__(self, n):
        self.str_len = n

    def get_strings_of_n_bits(self, str_so_far='', str_index=-1):
        if str_index >= self.str_len - 1:
            yield str_so_far
            return

        ############################################################
        # Recursive Approach-1
        ############################################################
        for string in self.get_strings_of_n_bits(str_so_far + '0', str_index + 1):
            yield string

        for string in self.get_strings_of_n_bits(str_so_far + '1', str_index + 1):
            yield string

        ############################################################
        # Recursive Approach-2
        # (Wrong, as it skips each str-index once and consider once and we do not need to skip any index)
        ############################################################
        # for index in range(str_index + 1, self.str_len):
        #     for string in self.get_strings_of_n_bits(str_so_far + '0', index):
        #         yield string
        #     for string in self.get_strings_of_n_bits(str_so_far + '1', index):
        #         yield string
        ############################################################

    def print_all_permutations(self):
        count = 1
        for string in self.get_strings_of_n_bits():
            print(count, string)
            count += 1


# driver code
def run():
    # string = 'abcc'
    # print(f'All permutations of the string={string} are: \n')
    # StringPermutations(string).print_all_permutations()

    n = 4
    print(f'\nAll strings of {n}-bits are: \n')
    StringOfNBits(n).print_all_permutations()


if __name__ == '__main__':
    run()
