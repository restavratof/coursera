# https://cryptopals.com/sets/1

import codecs

# --------------------------------------------------------------------------------------------------------
# --- FUNCTIONS
# --------------------------------------------------------------------------------------------------------
def section_start(name):
    print('-' * 100)
    print('-', name)
    print('-' * 100)


def hex_to_base64(value):
    return codecs.encode(codecs.decode(value, 'hex'), 'base64').decode()

print('-' * 100)
print('-', 'Challenge 1 - Convert hex to base64:')
print('-' * 100)
in_1='49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
out_1 = hex_to_base64(in_1)
print(f'IN: {in_1}')
print(f'OUT: {out_1}')