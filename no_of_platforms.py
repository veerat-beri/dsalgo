# Problem Statement:
# https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/


def calculate_max_platforms(arrival_time_arr, departure_time_arr):
    arrival_time_arr_len = len(arrival_time_arr)
    departure_time_arr_len = len(departure_time_arr)
    if arrival_time_arr_len != departure_time_arr_len:
        return -1

    arr_time_arr_index = 0
    departure_time_arr_index = 0
    max_tracks_req = 0
    no_of_tracks_at_given_point = 0

    while arr_time_arr_index < arrival_time_arr_len and ----:
        if arrival_time_arr[arr_time_arr_index] < departure_time_arr[departure_time_arr_index]:
            no_of_tracks_at_given_point += 1
            if max_tracks_req < no_of_tracks_at_given_point:
                max_tracks_req += 1
            arr_time_arr_index += 1
        else:
            no_of_tracks_at_given_point -= 1
            departure_time_arr_index += 1

    return max_tracks_req

# driver code

calculate_max_platforms()
