# Problem Statement
# https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/

NO_OF_CHARS = 256


def are_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    count_arr = [0] * NO_OF_CHARS
    for char in str1:
        count_arr[ord(char)] += 1

    for char in str2:
        count_arr[ord(char)] -= 1

    for freq in count_arr:
        if freq:
            return False

    return True


# driver code
def run():
    str1 = 'geeksforgeeks'  # 'test'
    str2 = 'forgeeksgeeks'  # 'ttew'

    print(f'Given strings: \nstr1: {str1}\nstr2: {str2}\n')
    if are_anagram(str1, str2):
        print('Yes, the two given strings are anagrams')
    else:
        print('No, the two given strings are not anagrams')


if __name__ == '__main__':
    run()
