# Problem Statement
# https://www.geeksforgeeks.org/searching-for-patterns-set-3-rabin-karp-algorithm/


class RabinKarpStringMatch:
    NO_OF_CHARS = 256
    PRIME_NUM = 11

    def __init__(self, pattern_str: str, text_str: str):
        self.pattern_str = pattern_str
        self.pattern_str_len = len(pattern_str)
        self.text_str = text_str
        self.text_str_len = len(text_str)
        self.h = self.__get_h_value()

    def __get_h_value(self):
        """
        :return: equivalent of => pow(NO_OF_CHARS, pattern_str_len - 1, PRIME_NUM)
        """
        ##############################
        h = 1
        for _ in range(self.pattern_str_len - 1):
            h = (h * self.NO_OF_CHARS) % self.PRIME_NUM
        return h
        ##############################
        # return pow(self.NO_OF_CHARS, self.pattern_str_len - 1, self.PRIME_NUM)

    def get_hash_values(self):
        pattern_hash = 0
        text_hash_so_far = 0

        for str_index in range(self.pattern_str_len):
            pattern_hash = (pattern_hash * self.NO_OF_CHARS + ord(self.pattern_str[str_index])) % self.PRIME_NUM
            text_hash_so_far = (self.NO_OF_CHARS * text_hash_so_far + ord(self.text_str[str_index])) % self.PRIME_NUM

        return pattern_hash, text_hash_so_far

    def pattern_matches(self, text_window_start_index):
        for str_index in range(self.pattern_str_len):
            if self.text_str[text_window_start_index + str_index] != self.pattern_str[str_index]:
                return False
        return True

    def __get_updated_text_window_hash(self, str_index, text_hash_so_far):
        return (self.NO_OF_CHARS * (text_hash_so_far - ord(self.text_str[str_index]) * self.h) + ord(self.text_str[str_index + self.pattern_str_len])) % self.PRIME_NUM

    def get_pattern_occurrence_indexes(self):
        max_pos_for_hash_computations = self.text_str_len - self.pattern_str_len
        pattern_hash, text_hash_so_far = self.get_hash_values()
        for str_index in range(max_pos_for_hash_computations + 1):
            if pattern_hash == text_hash_so_far and self.pattern_matches(str_index):
                yield str_index
            if str_index < max_pos_for_hash_computations:
                self.__get_updated_text_window_hash(str_index, text_hash_so_far)

# driver code
def run():
    text_str = 'AABAACAADAABAABA'
    pattern_str = 'AABA'

    print('\nText String: \n{}'.format(text_str))
    print(f'Pattern String: {pattern_str}')
    print('Pattern found at indexes: ')
    for pattern_occurrence_index in RabinKarpStringMatch(pattern_str, text_str).get_pattern_occurrence_indexes():
        # print(text_str[pattern_occurrence_index: pattern_occurrence_index + len(pattern_str)])
        print(pattern_occurrence_index)


if __name__ == '__main__':
    run()
