# https://cryptopals.com/sets/1

import codecs
from collections import Counter

print('-' * 100)
print('-', f'Challenge 1 - Single-byte XOR cipher:')
print('-' * 100)

hex_enc_str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

bytes_str = bytes.fromhex(hex_enc_str)
# print(f'BYTES: {bytes_str}')
bytes_str_len = len(bytes_str)

all_list = [ ' ', '!', '#', '$', '%', '&', '`', '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', ']', '^', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~' ]
letters_list = [ ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
cnt = Counter()

def xor(bytes_strA, bytes_strB):
    return bytes(a^b for a, b in zip(bytes_strA, bytes_strB))


for ch in all_list:
    ch_long = ch*bytes_str_len
    result = xor(bytes_str, ch_long.encode())
    # print(f'{ch} : {result}')
    text_result = result.decode()
    # print(f'  - {text_result}')
    # count letters in results
    for ch1 in text_result:
        if ch1 in letters_list:
            cnt[ch] += 1


# Check and save result
for item, frequency in cnt.most_common(1):
    result_key = item

result_bytes = xor(bytes_str, (result_key*bytes_str_len).encode())
result_msg = result_bytes.decode()

print(f'RESULT:  {result_key} - {result_msg}')

