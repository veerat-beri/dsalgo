# Problem Statement
# https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
from strings.services import swap_chars


def get_all_permutations(string: str):
    str_len = len(string)

    def _get_all_permutations(str_so_far: str, fixed_index: int):
        if fixed_index == str_len - 1:
            print(str_so_far)
            return

        for str_index in range(fixed_index, str_len):
            swapped_str = swap_chars(str_so_far, fixed_index, str_index)
            _get_all_permutations(swapped_str, fixed_index + 1)

    _get_all_permutations(string, 0)


# driver code
def run():
    string = 'abc'
    get_all_permutations(string)
    # for permuted_string in get_all_permutations(string):
    #     print(permuted_string)


if __name__ == '__main__':
    run()
