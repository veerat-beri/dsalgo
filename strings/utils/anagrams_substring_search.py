# Problem Statement
# https://www.geeksforgeeks.org/anagram-substring-search-search-permutations/

from collections import defaultdict
from copy import copy


class AnagramSubstringSearch:
    def __init__(self, pattern_str: str, text_str: str):
        self.pattern_str = pattern_str
        self.text_str = text_str
        self.pattern_str_len = len(pattern_str)
        self.text_str_len = len(text_str)
        self.__pattern_char_count_dict = self.__get_patter_str_chars_count()
        self.__whitelisted_str_index = None

    def __should_remove_char(self, present_str_index):
        # This is done to remove ambiguity in judging whether
        # to consider chars from previous window(in case pattern chars are matching successively)
        # or not consider them (when previous window has chars which do not belong to pattern string)
        if self.__whitelisted_str_index and self.__whitelisted_str_index >= present_str_index:
            return False
        return True

    def __set_white_listed_str_index(self, str_index):
        self.__whitelisted_str_index = str_index

    @property
    def pattern_char_count_dict(self):
        # Made property to make sure "__pattern_char_count_dict" is read-only and can not be changed
        return self.__pattern_char_count_dict

    def __update_text_window_extra_chars_count(self, char, count_increment, text_window_extra_chars_count):
        text_window_extra_chars_count[char] += count_increment

        if not text_window_extra_chars_count[char]:
            del text_window_extra_chars_count[char]

    def __remove_last_window_char(self, str_index, text_window_extra_chars_count):
        char_index_to_be_removed = str_index - self.pattern_str_len
        if char_index_to_be_removed >= 0 and self.__should_remove_char(char_index_to_be_removed):
            char = self.text_str[char_index_to_be_removed]
            self.__update_text_window_extra_chars_count(char, 1, text_window_extra_chars_count)

    def __add_new_window_char(self, str_index, text_window_extra_chars_count):
        char = self.text_str[str_index]
        self.__update_text_window_extra_chars_count(char, -1, text_window_extra_chars_count)

    def __reset_text_window_extra_chars_count(self):
        return copy(self.pattern_char_count_dict)

    def __get_patter_str_chars_count(self):
        patter_str_chars_count = defaultdict(int)
        for char in self.pattern_str:
            patter_str_chars_count[char] += 1

        return patter_str_chars_count

    def get_all_anagrams_pos(self):
        str_index = 0
        text_window_extra_chars_count = self.__reset_text_window_extra_chars_count()

        while str_index < self.text_str_len:
            if self.text_str[str_index] not in self.pattern_char_count_dict:
                text_window_extra_chars_count = self.__reset_text_window_extra_chars_count()
                self.__set_white_listed_str_index(str_index)
            else:
                self.__remove_last_window_char(str_index, text_window_extra_chars_count)
                self.__add_new_window_char(str_index, text_window_extra_chars_count)

            if not text_window_extra_chars_count:
                print(str_index - self.pattern_str_len + 1)
            str_index += 1


# driver code
def run():
    # pattern_str = 'ABCD'
    # text_str = 'BACDGABCDA'
    pattern_str = 'AABA'
    text_str = 'AAABABAA'
    AnagramSubstringSearch(pattern_str, text_str).get_all_anagrams_pos()


if __name__ == '__main__':
    run()
