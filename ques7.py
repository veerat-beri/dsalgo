
arr = [100, 180, 260, 310, 40, 535, 695, ]
r_max, max_diff = 0, 0
for index in range(0, len(arr), -1):
    if arr[index] > r_max:
        r_max = arr[index]
    while :
        diff = r_max - arr[index]
        if max_diff < diff:
