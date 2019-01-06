def r(n, k):
    l_n = pow(10, 9) + 7

    return ((((k-1) ** (n-1))%l_n)*k)%l_n

t = int(input())
for _ in range(t):
    n, k = list(map(int, input().strip().split()))
    print(r(n, k))