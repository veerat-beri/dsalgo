# Problem statement
# https://www.geeksforgeeks.org/count-distinct-elements-in-every-window-of-size-k/

def get_every_subarray_distinct_count(arr, subarray_window_size):
    current_subarray_elem_count = {}
    for index in range(subarray_window_size):
        

