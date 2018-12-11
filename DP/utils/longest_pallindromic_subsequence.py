# Problem Statement
# https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/


def get_longest_palindromic_subsequence(input_str):
    def _get_longest_palindromic_subsequence(start_index, end_index):
        if start_index >= end_index:
            return 0
        if input_str[start_index] == input_str[end_index]:
            return 1 + _get_longest_palindromic_subsequence(start_index + 1, end_index - 1)
        return max(_get_longest_palindromic_subsequence(start_index + 1, end_index),
                   _get_longest_palindromic_subsequence(start_index, end_index - 1)) + 1

    return _get_longest_palindromic_subsequence(input_str[0], input_str[-1])


# driver code
def run():
    input_str = "geeksforgeeks"
    print('Longest Palindromic Subsequence length is: ', end='')
    print(get_longest_palindromic_subsequence(input_str))


if __name__ == ''



