import codecs

print('Challenge 1','-'*30)
str='49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
print(str)
b64 = codecs.encode(codecs.decode(str, 'hex'), 'base64').decode()
print(b64)


print('Challenge 2','-'*30)


def fixed_xor(str1, str2):
    return ''.join(x^y for x,y in zip(str1, str2))

def strxor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

str1 = '1c0111001f010100061a024b53535009181c'
str2 = '686974207468652062756c6c277320657965'

result = strxor(str1, str2)
print(result.encode().hex())

