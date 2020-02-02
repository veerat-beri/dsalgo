# Problem Statement
# https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/
# https://leetcode.com/problems/3sum/

from arrays.utils.pair_with_given_sum import PairWithGivenSum


class TripletWithGivenSum(PairWithGivenSum):

    # Hash based Approach
    def _using_hashing(self, required_sum, arr_start_index=0):
        # Time Complexity: O(n^2)
        # Space Complexity: O(n)

        triplet_found = False
        for arr_index in range(self.arr_len - 2):
            elem = self.arr[arr_index]
            required_pair_sum = required_sum - elem
            for pair in super()._using_hashing(required_sum=required_pair_sum, arr_start_index=arr_index + 1):
                triplet_found = True
                yield (*pair, elem)

            if triplet_found and self.only_one_result:
                break

    # Sorting based Approach
    def _using_sorting(self, required_sum):
        # Time Complexity: O(N*logN + N^2) ~ O(N^2)
        # Space Complexity: O(1)
        self.arr.sort()
        arr_index = 0

        while arr_index < self.arr_len - 2:
            elem = self.arr[arr_index]

            if self.only_unique_pairs and arr_index and elem == self.arr[arr_index - 1]:
                arr_index += 1
                continue

            start_index = arr_index + 1
            end_index = self.arr_len - 1
            latest_unique_pair_elem = set()
            required_pair_sum = required_sum - elem

            while start_index < end_index:
                elem1 = self.arr[start_index]
                elem2 = self.arr[end_index]
                if elem1 + elem2 == required_pair_sum:
                    start_index += 1
                    end_index -= 1

                    if self.only_unique_pairs and latest_unique_pair_elem and elem2 in latest_unique_pair_elem and elem1 in latest_unique_pair_elem:
                        continue

                    latest_unique_pair_elem = {elem1, elem2}
                    yield elem1, elem2, elem

                    if self.only_one_result:
                        break

                elif elem1 + elem2 < required_pair_sum:
                    start_index += 1
                else:
                    end_index -= 1

            arr_index += 1


# driver code
def run():
    arr = [1, 4, 45, 6, 10, 8, 12, 12, 6, ]
    triplet_sum = 22
    triplets = TripletWithGivenSum(
        arr,
        unique=True,
        method=TripletWithGivenSum.USE_SORTING
    ).get_results(required_sum=triplet_sum)

    print(f'Given arr: {arr}\n')
    print(f'Triplets with sum = ({triplet_sum}) are: ')
    for triplet in triplets:
        print(f'{triplet[0]}, {triplet[1]}, {triplet[2]}')


if __name__ == '__main__':
    run()
