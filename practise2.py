VOWELS = ['a', 'e', 'i', 'o', 'u']


def can_append(vowel1, vowel2):
    if (vowel1 == 'a' and vowel2 == 'e') or (vowel1 == 'e' and vowel2 in {'a', 'i'}) or (vowel1 == 'o' and vowel2 in {'i', 'u'}) or (vowel1 == 'u' and vowel2 == 'a'):
        return True
    return False


def get_permutations(curr_char, str_len, permutation_count: []):
    if str_len <= 0:
        permutation_count[0] = permutation_count[0] + 1
        return

    for vowel in VOWELS:
        if can_append(curr_char, vowel):
            get_permutations(vowel, str_len - 1, permutation_count)


str_len = int(input().strip())
permutation_count = [0]

for vowel in VOWELS:
    get_permutations(vowel, str_len, permutation_count)

print(permutation_count[0])
