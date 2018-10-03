# Problem Statement:
# https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/


def calculate_min_platforms(arrival_time_arr, departure_time_arr):
    arrival_time_arr.sort()
    departure_time_arr.sort()

    arrival_time_arr_len = len(arrival_time_arr)
    departure_time_arr_len = len(departure_time_arr)
    if arrival_time_arr_len != departure_time_arr_len:
        return -1

    arr_time_arr_index = 0
    departure_time_arr_index = 0
    min_tracks_req = 0
    no_of_tracks_at_given_point = 0

    while arr_time_arr_index < arrival_time_arr_len and departure_time_arr_index < departure_time_arr_len:
        if arrival_time_arr[arr_time_arr_index] < departure_time_arr[departure_time_arr_index]:
            no_of_tracks_at_given_point += 1
            if min_tracks_req < no_of_tracks_at_given_point:
                min_tracks_req += 1
            arr_time_arr_index += 1
        else:
            no_of_tracks_at_given_point -= 1
            departure_time_arr_index += 1

    return min_tracks_req


# driver code
arrival_time_arr = [900, 940, 950, 1100, 1500, 1800]
departure_time_arr = [910, 1200, 1120, 1130, 1900, 2000]

min_tracks_required = calculate_min_platforms(arrival_time_arr, departure_time_arr)
print(min_tracks_required)
