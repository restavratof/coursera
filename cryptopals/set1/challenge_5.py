# https://cryptopals.com/sets/1/challenges/5
# --- Implement repeating-key XOR
# Here is the opening stanza of an important work of the English language:
#       Burning 'em, if you ain't quick and nimble
#       I go crazy when I hear a cymbal
# Encrypt it, under the key "ICE", using repeating-key XOR.
# In repeating-key XOR, you'll sequentially apply each byte of the key; the first byte of plaintext will be XOR'd
#   against I, the next C, the next E, then I again for the 4th byte, and so on.
# It should come out to:
#       0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
#       a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
# Encrypt a bunch of stuff using your repeating-key XOR function. Encrypt your mail. Encrypt your password file.
# Your .sig file. Get a feel for it. I promise, we aren't wasting your time with this.
# --------------------------------------------------------------------------------------------------------------------
import codecs
from collections import Counter
from os import strerror

#  One of the 60-character strings in this file has been encrypted by single-character XOR.
#  Find it.
print('-' * 100)
print('-', f'Challenge 5 - Implement repeating-key XOR:')
print('-' * 100)
in_data = """Burning 'em, if you ain't quick and nimble
       I go crazy when I hear a cymbal"""
in_data = "dima_hello"
in_key = "ICE"
result = list()

def repeated_key_xor(plain_text, key):
    # returns plain text by repeatedly xoring it with key
    pt = plain_text
    len_key = len(key)
    encoded = []

    for i in range(0, len(pt)):
        encoded.append(pt[i] ^ key[i % len_key])
    return bytes(encoded)

plain_text = b'Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal'
key = b'ICE'
print("Plain text: ", plain_text)
print("Encrypted as: ", repeated_key_xor(plain_text, key).hex())
