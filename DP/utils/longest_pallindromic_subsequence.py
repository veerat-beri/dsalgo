# Problem Statement
# https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/


def get_longest_palindromic_subsequence(input_str: str):
    def _get_longest_palindromic_subsequence(start_index: int, end_index: int):
        if start_index == end_index:
            return 1
        if input_str[start_index] == input_str[end_index] and start_index + 1 == end_index:
            return 2

        if input_str[start_index] == input_str[end_index]:
            return 2 + _get_longest_palindromic_subsequence(start_index + 1, end_index - 1)
        return max(_get_longest_palindromic_subsequence(start_index + 1, end_index),
                   _get_longest_palindromic_subsequence(start_index, end_index - 1))

    return _get_longest_palindromic_subsequence(0, len(input_str) - 1)


# driver code
def run():
    input_str = "geeksforgeeks"
    # input_str = "ee"
    print('Longest Palindromic Subsequence length is: ', end='')
    print(get_longest_palindromic_subsequence(input_str))


if __name__ == '__main__':
    run()
