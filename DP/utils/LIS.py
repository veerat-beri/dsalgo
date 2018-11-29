# Problem Statement
# https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/


def get_LIS_length(str1):
    def _get_LIS_length(untraversed_str_len):
        if untraversed_str_len == 0:
            return 0
        for str_index in range(untraversed_str_len - 1):
            return 1 + max(_get_LIS_length(untraversed_str_len - 1))

    return _get_LIS_length(len(str1))


