# https://cryptopals.com/sets/1

import codecs


print('-' * 100)
print('-', f'Challenge 1 - Convert hex to base64:')
print('-' * 100)

str='49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
print(str)
b64 = codecs.encode(codecs.decode(str, 'hex'), 'base64').decode()
print(b64)
