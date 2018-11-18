def find_LCS_length(str1, str2, str1_index, str2_index):
    if str1_index == -1:
        return str2_index
    if str2_index == -1:
        return str1_index
    if str1[str1_index] == str2[str2_index]:
        return find_LCS_length(str1, str2, str1_index - 1, str2_index - 1)

    return 1 + min(find_LCS_length(str1, str2, str1_index - 1, str2_index),  # delete
                   find_LCS_length(str1, str2, str1_index, str2_index - 1),  # insert
                   find_LCS_length(str1, str2, str1_index - 1, str2_index - 1),  # replace
                   )

print(find_LCS_length("saturday", "sunday", 7, 5))