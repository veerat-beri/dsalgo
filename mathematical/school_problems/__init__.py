
__all__ = [
    'find_nth_term', 'is_armstrong', 'get_decimal_from_binary', 'get_sum_of_digits',
    'is_num_pallindrome', 'get_reverse_of_num', 'get_gcd',
]

from .AP_series import find_nth_term
from .armstrong import is_armstrong
from .binary_to_decimal import get_decimal_from_binary
from .digits_sum_pallindrome import get_sum_of_digits, is_num_pallindrome
from .reverse_num import get_reverse_of_num
from .gcd import get_gcd
