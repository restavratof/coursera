# https://cryptopals.com/sets/1

import codecs
from collections import Counter

print('-' * 100)
print('-', f'Challenge 1 - Detect single-character XOR:')
print('-' * 100)


def xor(bytes_strA, bytes_strB):
    return bytes(a^b for a, b in zip(bytes_strA, bytes_strB))


in_file = 'chall4.txt'


