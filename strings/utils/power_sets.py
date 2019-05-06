# Problem Statement
# https://www.geeksforgeeks.org/power-set/
# https://www.geeksforgeeks.org/recursive-program-to-generate-power-set/


def get_power_set(string: str):
    # Recursive Approach
    str_len = len(string)

    def _get_power_set(str_index: int = 0, str_so_far: str = ''):
        print(str_so_far, str_index)
        if str_index < str_len:
            _get_power_set(str_index + 1, str_so_far + string[str_index])
            _get_power_set(str_index + 1, str_so_far)

    _get_power_set()


# driver code
def run():
    string = 'abc'
    get_power_set(string)


if __name__ == '__main__':
    run()
