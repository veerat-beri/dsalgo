def find_nth_term(a1, a2, n: int):
    d = a2 - a1
    return a1 + (n - 1) * d


# driver code
def run():
    total_test_cases = int(input())
    for test_case in range(total_test_cases):
        a1, a2 = map(int, input().strip().split())
        n = int(input())
        print(find_nth_term(a1, a2, n))


if __name__ == '__main__':
    run()