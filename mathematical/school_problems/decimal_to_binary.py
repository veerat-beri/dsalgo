# Problem Statement
# https://www.geeksforgeeks.org/program-decimal-binary-conversion/

from enum import Enum, auto, unique


@unique
class BinToDecEnum(Enum):
    USE_STR_FORMATTING = auto()
    USE_RECURSION = auto()
    USE_ITERATION = auto()


class BinaryToDecimal:
    def __init__(self, num, exec_method=BinToDecEnum.USE_RECURSION):
        self.num = num
        self.exec_method = exec_method

    def _using_iteration(self, num: int) -> str:
        res = ''
        while num:
            res += str(num % 2)
            num = num // 2

        return res[::-1]

    def _using_iteration_optmised(self, num: int) -> str:
        res = ''
        while num:
            res += str(num % 2)
            num = num // 2

        return res[::-1]

    def _using_recursion(self, num: int) -> str:
        if num <= 1:
            return '1'
        return self._using_recursion(num // 2) + str(num % 2)

    def _using_str_formatting(self, num):
        return '{:b}'.format(num)

    def get_binary(self):
        return {
            BinToDecEnum.USE_RECURSION: self._using_recursion,
            BinToDecEnum.USE_STR_FORMATTING: self._using_str_formatting,
            BinToDecEnum.USE_ITERATION: self._using_iteration,
        }[self.exec_method](self.num)


# driver code
def run():
    num = 12
    print(f'{num} to binary: {BinaryToDecimal(num, BinToDecEnum.USE_ITERATION).get_binary()}')


if __name__ == '__main__':
    run()
