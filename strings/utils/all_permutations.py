# Problem Statement
# https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/


def get_all_permutations(string: str):
    print(string)


# driver code
def run():
    string = 'abc'
    for permuted_string in get_all_permutations(string):
        print(permuted_string)


if __name__ == '__main__':
    run()
