# Problem Statement
# https://www.geeksforgeeks.org/recursive-program-to-generate-power-set/


def get_power_set(string: str):
    str_len = len(string)

    # Recursive Approach
    def _get_power_set(str_index: int = 0, str_so_far: str = ''):
        if str_index == str_len:
            yield str_so_far

        if str_index < str_len:
            for sub_str in _get_power_set(str_index + 1, str_so_far + string[str_index]):
                yield sub_str
            for sub_str in _get_power_set(str_index + 1, str_so_far):
                yield sub_str

    # different Recursive Approach
    def _get_power_set_appr_2(str_index: int = 0, str_so_far: str = ''):
        if str_index == str_len:
            print(str_so_far)
            return
        for successive_str_index in range(str_index + 1, str_len):
            _get_power_set_appr_2(successive_str_index, str_so_far + string[successive_str_index])


    # return _get_power_set()
    _get_power_set_appr_2()


# driver code
def run():
    string = 'abc'
    # for sub_str in get_power_set(string):
    #     print(sub_str)
    get_power_set(string)


if __name__ == '__main__':
    run()
