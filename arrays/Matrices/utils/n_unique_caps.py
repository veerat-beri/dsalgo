# Problem Statement
# https://www.geeksforgeeks.org/bitmasking-and-dynamic-programming-set-1-count-ways-to-assign-unique-cap-to-every-person/

from typing import List


# Recursive Approach
def get_total_arrangements(caps_collections: List[List[int]]):
    total_cap_collections = len(caps_collections)

    def _process_possible_arrangements(selected_caps_set, collection_index, possible_arrangements_count):
        if collection_index >= total_cap_collections:
            return possible_arrangements_count + 1

        caps_collection = caps_collections[collection_index]
        for cap in caps_collection:
            if cap in selected_caps_set:
                continue
            selected_caps_set.add(cap)
            possible_arrangements_count = _process_possible_arrangements(selected_caps_set, collection_index + 1, possible_arrangements_count)
            selected_caps_set.remove(cap)
        return possible_arrangements_count

    return _process_possible_arrangements(set(), 0, 0)

############################################################
# DP approach is covered in DP section
# /DP/utils/bitmasking/n_caps.py
############################################################


# driver code
def run():
    caps_collections = [
        [5, 100, 1, ],
        [2, ],
        [5, 100, ],
    ]

    print(f'Caps collections: {caps_collections}')
    print(f'Total number of ways to select unique cap from each set: {get_total_arrangements(caps_collections)}')


if __name__ == '__main__':
    run()
