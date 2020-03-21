# https://cryptopals.com/sets/1

import codecs
from collections import Counter

# Print challenge num
def print_challenge_by_num(num, name):
    print()
    print('-' * 100)
    print('-', f'Challenge {num} - {name}:')
    # print('-' * 100)

######################################################################################################
print_challenge_by_num(1, 'Convert hex to base64')
str='49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
# print(str)
b64 = codecs.encode(codecs.decode(str, 'hex'), 'base64').decode()
print(b64)

######################################################################################################
print_challenge_by_num(2, 'Fixed XOR')

def xor(bytes_strA, bytes_strB):
    return bytes(a^b for a, b in zip(bytes_strA, bytes_strB))

def fixed_xor(str1, str2):
    bytes_str1 = bytes.fromhex(str1)
    bytes_str2 = bytes.fromhex(str2)
    # print(f' * fixed_xor - BS1: {bytes_str1}')
    # print(f' * fixed_xor - BS2: {bytes_str2}')
    result = xor(bytes_str1, bytes_str2)
    # print(f' * fixed_xor - RES: {result}')
    return result.hex()

str1 = '1c0111001f010100061a024b53535009181c'
str2 = '686974207468652062756c6c277320657965'

print(fixed_xor(str1, str2))


######################################################################################################
print_challenge_by_num(3, 'Single-byte XOR cipher')

hex_enc_str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

bytes_str = bytes.fromhex(hex_enc_str)
# print(f'BYTES: {bytes_str}')
bytes_str_len = len(bytes_str)

all_list = [ ' ', '!', '#', '$', '%', '&', '`', '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', ']', '^', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~' ]
letters_list = [ ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
cnt = Counter()

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


######################################################################################################
print_challenge_by_num(4, 'Detect single-character XOR')
in_file = 'set1_chall4.txt'



######################################################################################################

######################################################################################################

######################################################################################################

######################################################################################################

######################################################################################################

