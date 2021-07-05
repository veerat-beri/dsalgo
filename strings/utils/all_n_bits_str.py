# Problem Statement
# https://www.geeksforgeeks.org/generate-all-the-binary-strings-of-n-bits/


class StringOfNBits:
    def __init__(self, n):
        self.str_len = n

    # Time Complexity: O(2^N)
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
        # (Wrong, as it skips each str-index once and consider once but we do not need to skip any index)
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
    n = 4
    print(f'\nAll strings of {n}-bits are: \n')
    StringOfNBits(n).print_all_permutations()


if __name__ == '__main__':
    run()
