# Problem Statement
# https://www.geeksforgeeks.org/anagram-substring-search-search-permutations/
from collections import defaultdict
from copy import copy


class AnagramSubstringSearch:
    def __init__(self, pattern_str: str, text_str: str):
        self.pattern_str = pattern_str
        self.text_str = text_str
        self.patter_str_char_count = defaultdict(int)

    def _init_present_window_char_count(self):
        return copy(self.patter_str_char_count)

    def _init_patter_str_char_count(self):
        for char in self.pattern_str:
            self.patter_str_char_count[char] += 1

    def get_all_anagrams_pos(self):
        for char in self.text_str:
            if


# driver code
def run():
    pattern_str = 'ABCD'
    text_str = 'BACDGABCDA'


if __name__ == '__main__':
    run()
