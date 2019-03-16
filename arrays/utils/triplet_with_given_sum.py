# Problem Statement
# https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/


def get_triplet_of_sum(arr: [], triplet_sum):
    # Hash Based Approach
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)

    arr_len = len(arr)
    for arr_index in range(arr_len - 2):
        arr_elem_so_far = set()
        required_pair_sum = triplet_sum - arr[arr_index]
        for sub_array_index in range(arr_index + 1, arr_len):
            another_elem_in_triplet = arr[sub_array_index]
            if required_pair_sum - another_elem_in_triplet in arr_elem_so_far:
                return arr[arr_index], required_pair_sum - another_elem_in_triplet, another_elem_in_triplet
            arr_elem_so_far.add(another_elem_in_triplet)


# driver code
def run():
    arr = [1, 4, 45, 6, 10, 8]
    triplet_sum = 22
    triplet_nums = get_triplet_of_sum(arr, triplet_sum)

    print(f'Given arr: {arr}')
    if triplet_nums:
        print(f'Yes Triplet with sum({triplet_sum}) exists: {triplet_nums[0]}, {triplet_nums[1]}, {triplet_nums[2]}')
        return
    print(f'No Triplet with sum({triplet_sum}) does not exists')


if __name__ == '__main__':
    run()
