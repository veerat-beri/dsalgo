# Problem Statement
# https://www.geeksforgeeks.org/print-all-combinations-of-given-length/


class AllStrings:
    def __init__(self, char_set: set, str_len: int):
        self.str_len = str_len
        self.char_set = char_set

    def _get_all_strings(self, str_so_far='', str_len_so_far=0):
        if str_len_so_far == self.str_len:
            yield str_so_far
            return

        for char in self.char_set:
            for str_perm in self._get_all_strings(str_so_far + char, str_len_so_far + 1):
                yield str_perm

    def print_all_str(self):
        count = 1
        for string in self._get_all_strings():
            print(count, string)
            count += 1


# driver code
def run():
    char_set = {'a', 'b'}
    str_len = 3

    print(f'All strings of the len={str_len} with given chars={char_set} are: \n')
    AllStrings(char_set=char_set, str_len=str_len).print_all_str()


if __name__ == '__main__':
    run()
