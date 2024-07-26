# Problem Statement
# https://leetcode.com/problems/valid-palindrome/

def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not (s[left].isalnum()):
            left += 1
        while left < right and not (s[right].isalnum()):
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# driver code
def run():
    sample_string = ".,"
    print(f'"{sample_string}" is {"" if isPalindrome(sample_string) else "not "}Palindrome')

    sample_string = 'A man, a plan, a canal: Panama'
    print(f'"{sample_string}" is {"" if isPalindrome(sample_string) else "not "}Palindrome')

    sample_string = 'race a car'
    print(f'"{sample_string}" is {"" if isPalindrome(sample_string) else "not "}Palindrome')


if __name__ == '__main__':
    run()
