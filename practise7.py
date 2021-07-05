# Problem Statement
# https://leetcode.com/problems/first-missing-positive/submissions/

from typing import List


class Solution:
    def segregate_arr(self, arr: []):
        start_index = 0
        end_index = len(arr) - 1
        while start_index < end_index:
            if arr[start_index] > 0:
                arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
                end_index -= 1
            else:
                start_index += 1

        for index in range(len(arr)):
            if arr[index] > 0:
                return index
        return len(arr)

    # def update_positive_arr(self, arr: []):
    #     for index in range(len(arr)):
    #         elem = abs(arr[index])
    #         if elem - 1 >= len(arr):
    #             continue
    #
    #         if arr[elem - 1] < 0:
    #             continue
    #         arr[elem - 1] = -arr[elem - 1]
    #
    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     first_positive_index = self.segregate_arr(nums)
    #     # print(nums, first_positive_index)
    #     positive_arr = nums[first_positive_index:] if first_positive_index < len(nums) else []
    #     # print(positive_arr)
    #     self.update_positive_arr(positive_arr)
    #     # print("updated: ", positive_arr)
    #
    #     for index in range(len(positive_arr)):
    #         if positive_arr[index] > 0:
    #             return index + 1
    #
    #     return len(positive_arr) + 1

    def update_positive_arr(self, arr: [], first_positive_index):
        for index in range(first_positive_index, len(arr)):
            elem = abs(arr[index])
            if elem - 1 >= len(arr) - first_positive_index:
                continue

            if arr[first_positive_index + elem - 1] < 0:
                continue

            arr[first_positive_index + elem - 1] = -arr[first_positive_index + elem - 1]

    def firstMissingPositive(self, nums: List[int]) -> int:
        first_positive_index = self.segregate_arr(nums)

        print(nums, first_positive_index)
        self.update_positive_arr(nums, first_positive_index)
        print("updated: ", nums)

        for index in range(first_positive_index, len(nums)):
            if nums[index] > 0:
                return index + 1 - first_positive_index

        return len(nums) + 1 - first_positive_index


# driver code
def run():
    arr = [0]
    # arr = [-2, -11, -3, -4]
    # arr = [1, 0]
    # arr = [1, 1]
    # arr = [3, 4, -1, 1]
    print("Given array: ", arr)
    print(Solution().firstMissingPositive(arr))


if __name__ == '__main__':
    run()
