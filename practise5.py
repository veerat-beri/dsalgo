from typing import List


def get_intermediate_comb(num, seq):
    other_permutations = []
    for seq_index in range(len(seq) - 1):
        other_permutations.append([seq[seq_index]] + seq[:seq_index] + [num, ] + seq[seq_index + 1:])
    return other_permutations


def get_all_permutations(nums: List[int]) -> List[List[int]]:
    current_pos = 1
    temp_list = [nums[:current_pos]]

    while current_pos < len(nums):
        final_list = []
        for seq_comb in temp_list:
            current_num = nums[current_pos]
            final_list.append(seq_comb + [current_num, ])
            final_list.append([current_num, ] + seq_comb)
            final_list += get_intermediate_comb(current_num, seq_comb)

        current_pos += 1
        temp_list = final_list

    return temp_list



