# Problem Statement
# https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class LongestDistinctSubstring:
    #############################################
    # Time Complexity: O(N^2)
    # Space Complexity: O(256) ~= O(1)
    #############################################
    def longest_substr_len(self, s: str) -> int:
        res = 0
        for start_index in range(len(s)):
            chars_visited_in_substring = set()
            for end_index in range(start_index, len(s)):
                if s[end_index] in chars_visited_in_substring:
                    break
                chars_visited_in_substring.add(s[end_index])
                res = max(res, end_index - start_index + 1)
        return res

    #############################################
    # Time Complexity: O(N)
    # Space Complexity: O(256) ~= O(1)
    #############################################
    def longest_substr_len_optimised(self, s: str) -> int:
        res = 0
        substring_start_index = 0
        ####################
        # APPROACH 1
        ####################
        # chars_visited_in_substring = {}
        #
        # for index in range(len(s)):
        #     if s[index] in chars_visited_in_substring:
        #         substring_start_index = max(substring_start_index, chars_visited_in_substring[s[index]] + 1)
        #     res = max(res, index - substring_start_index)
        #     chars_visited_in_substring[s[index]] = index
        ####################
        # SLIGHTLY MORE OPTIMISED
        ####################
        visited_chars = [None] * 128

        for index in range(len(s)):
            char_already_visited_at = visited_chars[ord(s[index])]
            if (char_already_visited_at is not None) and (substring_start_index < char_already_visited_at + 1):
                substring_start_index = char_already_visited_at + 1

            res = max(res, index - substring_start_index + 1)
            visited_chars[ord(s[index])] = index

        return res


# driver code
def run():
    string = "abcabcbb"
    print(f"longest distinct substring for given string: \n{string}: {LongestDistinctSubstring().longest_substr_len_optimised(string)}")


if __name__ == '__main__':
    run()
