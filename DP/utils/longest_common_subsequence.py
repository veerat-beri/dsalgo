# Problem Statement
# https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/


def find_LCS_length(str1, str2, str1_index, str2_index):
    if str1_index == -1 or str2_index == -1:
        return 0
    if str1[str1_index] == str2[str2_index]:

        print(str1[str1_index])
        return 1 + find_LCS_length(str1, str2, str1_index - 1, str2_index - 1)

    return max(find_LCS_length(str1, str2, str1_index - 1, str2_index),
               find_LCS_length(str1, str2, str1_index, str2_index - 1))


# driver code
def run():
    str1 = "saturday"
    str2 = "sunday"

    print(find_LCS_length(str1, str2, len(str1) - 1, len(str2) - 1))


if __name__ == '__main__':
    run()
