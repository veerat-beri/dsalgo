# Problem Statement
# https://www.geeksforgeeks.org/anagram-substring-search-search-permutations/

# This Approach did not work, due to ambiguity in judging whether
# to consider chars from previous window(in case pattern chars are matching successively)
# or not consider them (when previous window has chars which do not belong to pattern string)
from collections import defaultdict
from copy import copy


class AnagramSubstringSearch:
    def __init__(self, pattern_str: str, text_str: str):
        self.pattern_str = pattern_str
        self.text_str = text_str
        self.pattern_str_len = len(pattern_str)
        self.text_str_len = len(text_str)
        self.text_window_extra_chars_count = dict()
        self.__reset_text_window_extra_chars_count()
        self.__pattern_char_count_dict = None
        self.__whitelisted_str_index = None

    def should_remove_char(self, present_str_index):
        if self.__whitelisted_str_index and self.__whitelisted_str_index < present_str_index:
            self.__whitelisted_str_index = None
            return False
        return True

    def __set_white_listed_str_index(self, str_index):
        self.__whitelisted_str_index = str_index

    @property
    def pattern_char_count_dict(self):
        if not self.__pattern_char_count_dict:
            self.__pattern_char_count_dict = self.__get_patter_str_chars_count()
        return self.__pattern_char_count_dict

    def __remove_last_window_char(self, str_index):
        char_index_to_be_removed = str_index - self.pattern_str_len
        if char_index_to_be_removed >= 0 and self.should_remove_char(char_index_to_be_removed):
            char = self.text_str[char_index_to_be_removed]

            # # If that char is part of pattern string
            # if self.pattern_char_count_dict.get(char):
            self.text_window_extra_chars_count[char] += 1

    def __add_new_window_char(self, str_index):
        char = self.text_str[str_index]
        self.text_window_extra_chars_count[char] -= 1

        if not self.text_window_extra_chars_count[char]:
            del self.text_window_extra_chars_count[char]

    def __reset_text_window_extra_chars_count(self):
        self.text_window_extra_chars_count = copy(self.pattern_char_count_dict)

    def __get_patter_str_chars_count(self):
        patter_str_chars_count = defaultdict(int)
        for char in self.pattern_str:
            patter_str_chars_count[char] += 1

        return patter_str_chars_count

    def get_all_anagrams_pos(self):
        str_index = 0
        while str_index < self.text_str_len:
            if self.text_str[str_index] not in self.pattern_char_count_dict:
                self.__reset_text_window_extra_chars_count()
                self.__set_white_listed_str_index(str_index)
            else:
                self.__remove_last_window_char(str_index)
                self.__add_new_window_char(str_index)

            if not self.text_window_extra_chars_count:
                print(str_index - self.pattern_str_len + 1)
                # self.__remove_last_window_char(str_index)
# from strings.utils.string_matching.rabin_karp import RabinKarpStringMatch
#
#
# class AnagramSubstringSearch(RabinKarpStringMatch):
#     def _pattern_matches(self, text_window_start_index):
#         # No need to check for exact pattern match as any combination of pattern chars would work
#         return True


# driver code
def run():
    pattern_str = 'ABCD'
    text_str = 'BACDGABCDA'
    # pattern_str = 'AABA'
    # text_str = 'AAABABAA'
    AnagramSubstringSearch(pattern_str, text_str).get_all_anagrams_pos()
    # for substring_index in AnagramSubstringSearch(pattern_str, text_str).get_pattern_occurrence_indexes():
    #     # print(substring_index)
    #     pass


if __name__ == '__main__':
    run()
