# Problem Statement

# A company made a very large banner with a string S printed on it. The string S is formed by lowercase English
# alphabets. They wanted that in the string S, after K characters, the pattern printed should repeat i.e.
# suppose that S="herohero" and k=4 then you see that after 4 characters, again the word "hero" starts.
#
# By mistake, the string S did not follow this order. Now, you are given the task to correct the string S
# so that after every K characters the string begins to repeat. To change a character into another character
# the cost involved is the absolute difference between the positions of characters in the sequence of
# English alphabets. For e.g. if you want to change e to a or a to e then the cost is 5-1=4.
#
# Input:
#
# The first line contains a string S as input.
# The second line of input contains an integer K.
#
# Output:
#
# In the output, you need to print the minimum cost to convert the string S to a string which repeats itself
# after each interval of size K.
#
# Constraints:
#
# 1 <= |S| <= 10^5
# 1 <= K <=N

# Sample Input:
# aabaaabab
# 3
# Sample Output:
# 2
# Explanation:
# If we change the 6th character to "b" and 7th character to "a", then total cost involved is 2 which is the
# minimum cost to convert the string in the input.

#############################################################################################################
# SOLUTION
#############################################################################################################
import sys


def get_relative_difference(char1, char2='a'):
    return abs(ord(char1) - ord(char2))


def get_min_cost(input_str, window_size):
    def get_new_count_arr():
        return [0] * 26

    def _reset_count_arr(count_arr):
        for index in range(26):
            count_arr[index] = 0

    def _get_min_char_replacement_cost(count_arr):
        global_min_cost = sys.maxsize
        for replacing_char_index in range(26):
            local_min_cost = 0
            for replaced_char_index in range(26):
                local_min_cost += count_arr[replaced_char_index] * abs(replaced_char_index - replacing_char_index)
            global_min_cost = min(global_min_cost, local_min_cost)
        return global_min_cost

    cumulative_min_cost = 0
    for window_index in range(window_size):
        count_arr = get_new_count_arr()

        for str_index in range(window_index, len(input_str), window_size):
            count_arr[get_relative_difference(input_str[str_index])] += 1

        cumulative_min_cost += _get_min_char_replacement_cost(count_arr)

    return cumulative_min_cost


input_str = input().strip()
window_size = int(input())
print(get_min_cost(input_str, window_size))
