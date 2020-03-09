# # Problem Statement
#
#
# # Time Complexity: O(N) (Single Traversal)
# # Space Complexity: O(1)
# # Using Dutch National Flag Algorithm, or 3-way Partitioning
# # other ref: http://users.monash.edu/~lloyd/tildeAlgDS/Sort/Flag/
# from arrays.services import swap_arr_elem
#
#
# def segregate_0_1_2_3(arr: []):
#     arr_len = len(arr)
#     zeros_index = 0
#     ones_index = 0
#     twos_index = 0
#     threes_index = arr_len - 1
#     while twos_index <= threes_index:
#         # "<=" is required instead of obvious "<", as both zeros_index and twos_index
#         # are advanced 1 extra, each time and their (zeros_index/twos_index) last element will get
#         # skipped from checking, if "<" is used
#
#
#         # breakpoint()
#         if arr[twos_index] == 0:
#             swap_arr_elem(twos_index, zeros_index, arr)
#             zeros_index += 1
#             ones_index += 1
#             # twos_index += 1
#         elif arr[twos_index] == 1:
#             swap_arr_elem(twos_index, ones_index, arr)
#             ones_index += 1
#             twos_index += 1
#         elif arr[twos_index] == 3:
#             swap_arr_elem(twos_index, threes_index, arr)
#             threes_index -= 1
#         else:
#             twos_index += 1
#
#
# # driver code
# def run():
#     arr = [0, 1, 1, 0, 1, 2, 1, 2, 2, 0, 0, 1, 3, 2, 3]
#     print(f'Given array: \n{arr}')
#     segregate_0_1_2_3(arr)
#     print(f'\nArray after segregating 0, 1, 2, 3: \n{arr}')
#
#
# if __name__ == '__main__':
#     run()
