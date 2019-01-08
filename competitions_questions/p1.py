def get_set_bits_count(n):
    co = 0
    while (n):
        n &= (n - 1)
        co += 1

    return co


def get_ceil_of_arr(a, low, high, x):
    if x <= a[low]:
        return low

    if x > a[high]:
        return None

    mid = (low + high) // 2

    if a[mid] == x:
        return mid

    elif a[mid] < x:
        if mid + 1 <= high and x <= a[mid + 1]:
            return mid + 1
        else:
            return get_ceil_of_arr(a, mid + 1, high, x)

    else:
        if mid - 1 >= low and x > a[mid - 1]:
            return mid
        else:
            return get_ceil_of_arr(a, low, mid - 1, x)


bits_count_sum_list = []
st = 1


def u_a(ix):
    global st
    s = bits_count_sum_list[st]
    while s < ix:
        st += 1
        s += get_set_bits_count(st)
        bits_count_sum_list.append(s)


def make_bits_count_sum_list(e=10):
    global st
    p_s = 0

    for n in range(st, e + 1):
        p_s = get_set_bits_count(n) + p_s
        bits_count_sum_list.append(p_s)

    st = e - 1


total_test_cases = int(input())
make_bits_count_sum_list()

for _ in range(total_test_cases):
    ix = int(input())
    a = get_ceil_of_arr(bits_count_sum_list, 0, st, ix)
    if a is None:
        u_a(ix)
        print(st + 1)
    else:
        print(a + 1)

    # print(bits_count_sum_list)



