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
            text_hash_so_far = (text_hash_so_far * self.NO_OF_CHARS + ord(self.text_str[str_index])) % self.PRIME_NUM

        return pattern_hash, text_hash_so_far

    def check_text_window(self, text_window_start_index):
        for str_index in range(self.pattern_str_len):
            if self.text_str[text_window_start_index + str_index] != self.pattern_str[str_index]:
                return False
        return True

    def get_pattern_occurrences(self):
        pattern_occurrences_indexes = []
        pattern_hash, text_hash_so_far = self.get_hash_values()
        for str_index in range(self.text_str_len - self.pattern_str_len + 1):
            if pattern_hash == text_hash_so_far:
                if self.check_text_window(str_index):
                    pattern_occurrences_indexes.append(str_index)







# driver code
def run():
    pass


if __name__ == '__main__':
    run()
