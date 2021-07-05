# Problem Statement
# https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/

NO_OF_CHARS = 256


class CheckAnagram:
    USE_COUNT_ARR = 'COUNT_ARR'
    USE_BIT_MANIPULATION = 'BIT_MANIPULATION'

    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.str1_len = len(self.str1)

    def __is_valid_input(self):
        return self.str1_len == len(self.str2)

    #############################################
    # Method 1, using count-array
    # k = 256
    # Time Complexity: O(N) + O(k) =~ O(N)
    # Space Complexity: O(k) =~ O(1)
    def _using_count_arr(self):
        count_arr = [0] * NO_OF_CHARS

        for str_index in range(self.str1_len):
            count_arr[ord(self.str1[str_index])] += 1
            count_arr[ord(self.str2[str_index])] -= 1

        for freq in count_arr:
            if freq:
                return False

        return True

    #############################################
    # Method 2, using Bit-Manipulation
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    #############################################
    def _using_bit_manipulation(self):
        xorded_strs = 0
        for str_index in range(self.str1_len):
            xorded_strs ^= ord(self.str1[str_index])
            xorded_strs ^= ord(self.str2[str_index])
        return not xorded_strs
    #############################################

    def are_anagrams(self, choice=USE_BIT_MANIPULATION):
        if not self.__is_valid_input():
            return False
        exec_func = self._using_bit_manipulation if choice == self.USE_BIT_MANIPULATION else self._using_count_arr
        return exec_func()


# driver code
def run():
    str1 = 'geeksforgeeks'  # 'test'
    str2 = 'forgeeksgeeks'  # 'ttew'

    print(f'Given strings: \nstr1: {str1}\nstr2: {str2}\n')
    if CheckAnagram(str1, str2).are_anagrams():
        print('Yes, the two given strings are anagrams')
    else:
        print('No, the two given strings are not anagrams')


if __name__ == '__main__':
    run()
