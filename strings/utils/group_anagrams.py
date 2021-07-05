# Problem Statement
# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
from typing import List


def get_count_tuple(string):
    count_arr = [0 for _ in range(26)]
    for char in string:
        count_arr[ord(char) - ord('a')] += 1
    return tuple(count_arr)


def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagrams_grps = defaultdict(list)
    for string in strs:
        count_tuple = get_count_tuple(string)
        anagrams_grps[count_tuple].append(string)

    return list(anagrams_grps.values())


# driver code
def run():
    given_strs_arr = ["eat", "tea", "tan", "ate", "nat", "bat", ]
    print(group_anagrams(given_strs_arr))


if __name__ == '__main__':
    run()
