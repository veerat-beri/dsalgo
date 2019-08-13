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
        h = 0
        for _ in range(self.pattern_str_len):
            h = (h * self.NO_OF_CHARS) % self.PRIME_NUM
        return h

    def get_pattern_text_hash_values(self):
        pattern_hash = 0
        text_hash_so_far = 0

        for str_index in range(self.pattern_str_len):
            pattern_hash = (pattern_hash * self.NO_OF_CHARS + ord(self.pattern_str[str_index])) % self.PRIME_NUM
            text_hash_so_far = (text_hash_so_far * self.NO_OF_CHARS + ord(self.text_str[str_index])) % self.PRIME_NUM

        return pattern_hash, text_hash_so_far

    def get_pattern_occurrences(self):
        pattern_hash, text_hash_so_far = self.get_pattern_text_hash_values()
        # for str_index in range(self.text_str_len - self.pattern_str_len + 1):
        #     if pattern_hash == text_hash_so_far:
                # for char in



# driver code
def run():
    pass


if __name__ == '__main__':
    run()
