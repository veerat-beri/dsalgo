# Problem Statement
# https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/


def get_lps_arr(pattern_string: str):
    lps = [0]*len(pattern_string)
    local_max_prefix_len = 0
    str_index = 1
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


def get_all_pattern_occurrences(pattern_str: str, search_str: str, pattern_len: int):
    lps_arr = get_lps_arr(pattern_str)
    search_index = pattern_index = 0
    pattern_found_indexes = []

    while search_index < len(search_str):
        if search_str[search_index] == pattern_str[pattern_index]:
            pattern_index += 1
            search_index += 1
        else:
            if pattern_index > 0:
                pattern_index = lps_arr[pattern_index - 1]
            elif pattern_index <= 0:
                search_index += 1
                pattern_index = 0

        if pattern_index == pattern_len:
            pattern_found_indexes.append(search_index)
            pattern_index = lps_arr[pattern_index - 1]

    return pattern_found_indexes


# driver code
def run():
    pattern_str = 'ABABCABAB'
    search_str = 'ABABDABACDABABCABABABABCABAB'
    pattern_len = len(pattern_str)
    pattern_found_indexes = get_all_pattern_occurrences(pattern_str, search_str, pattern_len)

    if pattern_found_indexes:
        print('Pattern Found at: ')
        for index in pattern_found_indexes:
            print(index - pattern_len, end=' ')
    else:
        print('Pattern not found')


if __name__ == '__main__':
    run()
