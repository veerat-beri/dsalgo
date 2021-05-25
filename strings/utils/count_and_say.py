# Problem Statement
# https://leetcode.com/problems/count-and-say/

class CountSay:
    def say(self, prev_str):
        new_str = ''
        index = 0
        prev_str_len = len(prev_str)
        while index < prev_str_len:
            curr_char_count = 1
            while (index < prev_str_len - 1) and (prev_str[index] == prev_str[index + 1]):
                curr_char_count += 1
                index += 1

            new_str += str(curr_char_count) + str(prev_str[index])
            index += 1

        return new_str

    def count_and_say(self, n: int) -> str:
        str_so_far = ''
        for num in range(1, n + 1):
            if num == 1:
                str_so_far += '1'
                continue

            str_so_far = self.say(str_so_far)

        return str_so_far


    # def say(self, n):
    #     if n == 1:
    #         return '1'
    #
    #     prev_str = self.say(n - 1)
    #     new_str = ''
    #     # for key, val in Counter(prev_say_str).items():
    #     #     new_str = new_str + str(val) + str(key)
    #
    #     index = 0
    #     prev_str_len = len(prev_str)
    #     while index < prev_str_len:
    #         curr_char_count = 1
    #         while (index < prev_str_len - 1) and (prev_str[index] == prev_str[index + 1]):
    #             curr_char_count += 1
    #             index += 1
    #
    #         new_str += str(curr_char_count) + str(prev_str[index])
    #         index += 1
    #
    #     # print(new_str)
    #     return new_str
    #
    # def count_and_say(self, n: int) -> str:
    #     return self.say(n)


# driver code
def run():
    n = 6
    print(CountSay().count_and_say(n))


if __name__ == '__main__':
    run()
