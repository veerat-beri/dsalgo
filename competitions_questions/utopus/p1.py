from mathematical.utils import get_is_prime

c_s = {}


def pr():
    co = 0
    for n, s in c_s.items():
        if get_is_prime(s):
            co += 1
    return co


n = int(input())
for _ in range(n-1):
    n1, n2 = map(int, input().strip().split())
    c_s[n1] = c_s.get(n1, 0) + n2


print(pr())
