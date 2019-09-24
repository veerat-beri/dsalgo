# Problem Statement
# https://www.geeksforgeeks.org/bitmasking-and-dynamic-programming-set-1-count-ways-to-assign-unique-cap-to-every-person/

from typing import List


# Recursive Approach
def get_total_arrangements(caps_collections: List[List[int]]):
    possible_arrangements_count = 0
    total_cap_collections = len(caps_collections)

    def _process_possible_arrangements(selected_caps_set, collection_index):
        nonlocal possible_arrangements_count

        if collection_index >= total_cap_collections:
            possible_arrangements_count += 1
            return

        caps_collection = caps_collections[collection_index]
        for cap in caps_collection:
            if cap in selected_caps_set:
                continue
            selected_caps_set.add(cap)
            _process_possible_arrangements(selected_caps_set, collection_index + 1)
            selected_caps_set.remove(cap)

    _process_possible_arrangements(set(), 0)
    return possible_arrangements_count


# driver code
def run():
    caps_collections = [
        [5, 100, 1, ],
        [2, ],
        [5, 100, ],
    ]

    print(f'Total number of ways to select unique cap from each set: {get_total_arrangements(caps_collections)}')


if __name__ == '__main__':
    run()
