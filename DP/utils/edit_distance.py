# Problem Statement
# https://www.geeksforgeeks.org/edit-distance-dp-5/


# Recursive Approach
def get_min_edits_count(str1, str2):
    def _get_min_edits_count(str1_untraversed_len, str2_untraversed_len):
        if str1_untraversed_len == 0:
            # delete str2 if str1 is empty
            return str2_untraversed_len

        if str2_untraversed_len == 0:
            # delete str1 if str2 is empty
            return str1_untraversed_len

        if str1[str1_untraversed_len - 1] == str2[str2_untraversed_len - 1]:
            # continue traversing without any edit
            return _get_min_edits_count(str1_untraversed_len - 1, str2_untraversed_len - 1)

        return min(_get_min_edits_count(str1_untraversed_len - 1, str2_untraversed_len),  # delete a char from str1
                   _get_min_edits_count(str1_untraversed_len, str2_untraversed_len - 1),  # insert a char into str2
                   _get_min_edits_count(str1_untraversed_len - 1, str2_untraversed_len - 1),  # replace
                   ) + 1

    return _get_min_edits_count(len(str1), len(str2))
##########################################################################################


# driver code
def run():
    str1 = "saturday"
    str2 = "sunday"
    # str1 = "cat"
    # str2 = "cut"
    print('Minimum number of edits (operations) required to convert ‘str1’ into ‘str2’: ', get_min_edits_count(str1, str2))


if __name__ == '__main__':
    run()
