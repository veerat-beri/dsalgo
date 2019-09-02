# Problem Statement
# https://www.geeksforgeeks.org/anagram-substring-search-search-permutations/

# This Approach did not work, due to ambiguity in judging whether
# to consider chars from previous window(in case pattern chars are matching successively)
# or not consider them (when previous window has chars which do not belong to pattern string)
# class AnagramSubstringSearch:
#     def __init__(self, pattern_str: str, text_str: str):
#         self.pattern_str = pattern_str
#         self.text_str = text_str
#         self.pattern_str_len = len(pattern_str)
#         self.patter_str_chars_count = defaultdict(int)
#         self.required_chars_count = dict()
#         self._init_patter_str_chars_count()
#         self._reset_required_chars_count()
#
#     def _increase_required_char_count(self, str_index):
#         required_str_index = str_index - self.pattern_str_len
#         if required_str_index >= 0:
#             char = self.text_str[required_str_index]
#
#             # If that char is part of pattern string
#             if self.patter_str_chars_count.get(char):
#                 self.required_chars_count[char] += 1
#
#     def _reduce_required_char_count(self, str_index):
#         char = self.text_str[str_index]
#         self.required_chars_count[char] -= 1
#
#         if not self.required_chars_count[char]:
#             del self.required_chars_count[char]
#
#     def _reset_required_chars_count(self):
#         self.required_chars_count = copy(self.patter_str_chars_count)
#
#     def _init_patter_str_chars_count(self):
#         for char in self.pattern_str:
#             self.patter_str_chars_count[char] += 1
#
#     def get_all_anagrams_pos(self):
#         for str_index in range(len(self.text_str)):
#             if self.text_str[str_index] not in self.patter_str_chars_count:
#                 self._reset_required_chars_count()
#             else:
#                 self._increase_required_char_count(str_index)
#                 self._reduce_required_char_count(str_index)
#
#             if not self.required_chars_count:
#                 print(str_index - self.pattern_str_len + 1)
#                 # self._increase_required_char_count(str_index)
from strings.utils.string_matching.rabin_karp import RabinKarpStringMatch


class AnagramSubstringSearch(RabinKarpStringMatch):
    def _pattern_matches(self, text_window_start_index):
        # No need to check for exact pattern match as any combination of pattern chars would work
        return True


# driver code
def run():
    pattern_str = 'ABCD'
    text_str = 'BACDGABCDA'
    # pattern_str = 'AABA'
    # text_str = 'AAABABAA'
    for substring_index in AnagramSubstringSearch(pattern_str, text_str).get_pattern_occurrence_indexes():
        # print(substring_index)
        pass


if __name__ == '__main__':
    run()
