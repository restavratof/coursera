# https://cryptopals.com/sets/1

import codecs
from collections import Counter
from os import strerror

#  One of the 60-character strings in this file has been encrypted by single-character XOR.
#  Find it.
print('-' * 100)
print('-', f'Challenge 1 - Detect single-character XOR:')
print('-' * 100)

in_file = 'challenge4.txt'

result_count = 0
result_key = ''
result_msg = ''
#-----------------------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------------------
def xor(bytes_strA, bytes_strB):
    return bytes(a^b for a, b in zip(bytes_strA, bytes_strB))

def check_if_hex_enc_with_one_char(hex_str):
    global result_count
    bytes_str = bytes.fromhex(hex_str)
    # print(f'BYTES: {bytes_str}')
    bytes_str_len = len(bytes_str)
    all_list = [' ', '!', '#', '$', '%', '&', '`', '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5',
                '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', ']', '^', '_', 'a',
                'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                'w', 'x', 'y', 'z', '{', '|', '}', '~']
    letters_list = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                    'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    cnt = Counter()


    for ch in all_list:
        ch_long = ch*bytes_str_len
        result = xor(bytes_str, ch_long.encode())
        # print(f'{ch} : {result}')
        try:
            text_result = result.decode()
        except UnicodeDecodeError:
            continue
        # text_result = result.decode('latin-1')
        # print(f'  - {text_result}')
        # count letters in results
        for ch1 in text_result:
            if ch1 in letters_list:
                cnt[ch] += 1

    # Check and save result
    for item, frequency in cnt.most_common(1):
        tmp_key = item
        tmp_bytes = xor(bytes_str, (tmp_key * bytes_str_len).encode())
        try:
            tmp_msg = tmp_bytes.decode()
        except UnicodeDecodeError:
            continue
        print(f'RESULT: {frequency} - {tmp_key} - {tmp_msg}')

        if (frequency > result_count):
            result_count = frequency
            result_key = item
            result_msg = tmp_msg




#-----------------------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------------------


try:
    lcnt = 0
    for line in open(in_file, 'rt', encoding='latin-1'):
        lcnt += 1
        # if (lcnt == 3):
        #     break
        print(f'{lcnt} - {len(line)} : {line}')
        # print(f'        {bytes.fromhex(line)}')
        # CODE HERE
        check_if_hex_enc_with_one_char(line)

    print("Lines in file:       ", lcnt)
except IOError as e:
    print("I/O error occured: ", strerror(e.errno))

print(f'{result_count} - {result_key} - {result_msg}')






