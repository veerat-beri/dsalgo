# Problem Statement
# https://www.geeksforgeeks.org/recursive-program-to-generate-power-set/


def get_power_set(string: str):
    str_len = len(string)

    ############################################################
    # Recursive Approach-1
    ############################################################
    def _get_power_set(str_index: int = 0, str_so_far: str = ''):
        if str_index == str_len:
            yield str_so_far

        if str_index < str_len:
            for sub_str in _get_power_set(str_index + 1, str_so_far + string[str_index]):
                yield sub_str
            for sub_str in _get_power_set(str_index + 1, str_so_far):
                yield sub_str

    def _print_power_set(str_index: int = 0, str_so_far: str = ''):
        if str_index == str_len:
            print(str_so_far)

        if str_index < str_len:
            _print_power_set(str_index + 1, str_so_far + string[str_index])
            _print_power_set(str_index + 1, str_so_far)

    # return _get_power_set()
    # _print_power_set()

    ############################################################
    # Recursive Approach-2
    ############################################################
    def _get_power_set_approach_2(str_index: int = -1, str_so_far: str = ''):
        yield str_so_far
        for successive_str_index in range(str_index + 1, str_len):
            for sub_str in _get_power_set_approach_2(successive_str_index, str_so_far + string[successive_str_index]):
                yield sub_str

    def _print_power_set_approach_2(str_index: int = -1, str_so_far: str = ''):
        print(str_so_far)
        for successive_str_index in range(str_index + 1, str_len):
            _print_power_set_approach_2(successive_str_index, str_so_far + string[successive_str_index])

    # return _get_power_set_approach_2()
    _print_power_set_approach_2()

    ############################################################
    # Iterative Approach
    ############################################################
    # Its covered under bit-manipulation app


# driver code
def run():
    string = 'abc'
    # for sub_str in get_power_set(string):
    #     print(sub_str)
    get_power_set(string)


if __name__ == '__main__':
    run()
