# https://cryptopals.com/sets/1


print('-' * 100)
print('-', f'Challenge 2 - Fixed XOR:')
print('-' * 100)


def xor(bytes_strA, bytes_strB):
    return bytes(a^b for a, b in zip(bytes_strA, bytes_strB))

def fixed_xor(str1, str2):
    bytes_str1 = bytes.fromhex(str1)
    bytes_str2 = bytes.fromhex(str2)
    print(f' * fixed_xor - BS1: {bytes_str1}')
    print(f' * fixed_xor - BS2: {bytes_str2}')
    result = xor(bytes_str1, bytes_str2)
    print(f' * fixed_xor - RES: {result}')
    return result.hex()

str1 = '1c0111001f010100061a024b53535009181c'
str2 = '686974207468652062756c6c277320657965'

print(fixed_xor(str1, str2))
