# Problem Statement
# https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/


def find_LCS_length(str1, str2):

    def _find_LCS_length(str1_index, str2_index):
        if str1_index == -1 or str2_index == -1:
            return 0
        if str1[str1_index] == str2[str2_index]:
            return 1 + _find_LCS_length(str1_index - 1, str2_index - 1)

        return max(_find_LCS_length(str1_index - 1, str2_index),
                   _find_LCS_length(str1_index, str2_index - 1))

    return _find_LCS_length(len(str1) - 1, len(str2) - 1)


# driver code
def run():
    str1 = "saturday"
    str2 = "sunday"

    print('Length of Longest Common Sub-sequence: ', find_LCS_length(str1, str2))


if __name__ == '__main__':
    run()
