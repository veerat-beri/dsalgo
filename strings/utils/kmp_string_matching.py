# Problem Statement
# https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/


def get_lps_arr(pattern_string: str):
    lps = [0]*len(pattern_string)
    local_max_prefix_len = 0
    str_index = 1
    # for str_index in range(1, len(pattern_string)):
    while str_index < len(pattern_string):
        if pattern_string[str_index] == pattern_string[local_max_prefix_len]:
            local_max_prefix_len += 1
            lps[str_index] = local_max_prefix_len
            str_index += 1
        else:
            if local_max_prefix_len > 0:
                local_max_prefix_len = lps[local_max_prefix_len - 1]
            else:
                lps[str_index] = 0
                str_index += 1

    return lps


def get_all_pattern_occurrences(pattern_str: str, search_str: str):
    lps_arr = get_lps_arr(pattern_str)


    print(lps_arr)


# driver code
def run():
    pattern_str = 'AAACAAAA'
    search_str = ''
    get_all_pattern_occurrences(pattern_str, search_str)


if __name__ == '__main__':
    run()