# Problem Statement
# https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/


def get_lps_arr(pattern_string: str):
    lps = [0]*len(pattern_string)
    local_max_prefix_len = 0
    for str_index in range(1, len(pattern_string)):
        if pattern_string[str_index] == pattern_string[local_max_prefix_len]:
            local_max_prefix_len += 1
        else:
            while local_max_prefix_len > 0 and pattern_string[str_index] == pattern_string[local_max_prefix_len]:
                local_max_prefix_len = lps[local_max_prefix_len - 1]

        lps[str_index] = local_max_prefix_len
    return lps


def get_all_pattern_occurances():
    pass