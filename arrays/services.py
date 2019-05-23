from typing import Union


def swap_arr_elem(index1: int, index2: int, arr: Union[list, str]):
    arr[index1], arr[index2] = arr[index2], arr[index1]
