import codecs

separator = '-'*100
#--------------------------------------------------------------------------------
# Part 1: Bob -> Eve
#--------------------------------------------------------------------------------
print(separator)
print('-','Part 1: Bob -> Eve')

def xor(a, b):
    return bytes(x^y for x, y in zip(a, b))

print(xor(b'Bob', b'Eve').hex())
# >> '071907'


#--------------------------------------------------------------------------------
# Part 2: Dawn -> Dusk
#--------------------------------------------------------------------------------
print(separator)
print('-','Part 2: Dawn -> Dusk')

c = "6c73d5240a948c86981bc294814d"
# c = '09e1c5f70a65ac519458e7e53f36'

def strxor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))


c = codecs.decode("6c73d5240a948c86981bc294814d", 'hex')
print(f"1:   c(enc): {c}")

m1 = "attack at dawn".encode()
print(f"2: m1 (enc): {m1}")

m2 = "attack at dusk".encode()
print(f"3: m2 (enc): {m2}")

r1 = xor(c, m1)
print(f"4:         : {r1}")

r2 = xor(r1, m2)
print(f"5:         : {r2}")

result = codecs.encode(r2, 'hex')
print(f"6: result  : {result}")
# >>>'6c73d5240a948c86981bc2808548'
print(f'7: result  : {codecs.encode(xor(xor(codecs.decode("6c73d5240a948c86981bc294814d", "hex"), "attack at dawn".encode()), "attack at dusk".encode()), "hex")}')
# >>>'6c73d5240a948c86981bc2808548'

print('5','-'*30)
print('-','Part 3: ')
# Example:  hex of 'a' = 61  hex of space = 20 XOR 'a' and space = 41 = 'A' (in hex)
# same as:  hex of 'z' = 7A  hex of space = 20 XOR 'z' and space = 5A = 'Z' (in hex)

print(xor(b'a', b' ').hex())
print(xor(b'a', b' '))

ch = 'A'
print(f"'{ch}' hex({ch.encode().hex()}) binary({bin(ord(ch))})")
#    'A'  hex(41) binary(01000001)


print('5','-'*30)
all_list = [ ' ', '!', '#', '$', '%', '&', '`', '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', ']', '^', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~' ]
for ch in all_list:
    print(f"'{ch}': {ord(ch)}  : {ch.encode()} : {bin(ord(ch))} : {xor(ch.encode(), b' ')}")



all_dict = {
'!': '21',
'#': '23',
'$': '24',
'%': '25',
'&': '26',
'`': '60',
'(': '28',
')': '29',
'*': '2a',
'+': '2b',
',': '2c',
'-': '2d',
'.': '2e',
'/': '2f',
'0': '30',
'1': '31',
'2': '32',
'3': '33',
'4': '34',
'5': '35',
'6': '36',
'7': '37',
'8': '38',
'9': '39',
':': '3a',
';': '3b',
'<': '3c',
'=': '3d',
'>': '3e',
'?': '3f',
'@': '40',
'A': '41',
'B': '42',
'C': '43',
'D': '44',
'E': '45',
'F': '46',
'G': '47',
'H': '48',
'I': '49',
'J': '4a',
'K': '4b',
'L': '4c',
'M': '4d',
'N': '4e',
'O': '4f',
'P': '50',
'Q': '51',
'R': '52',
'S': '53',
'T': '54',
'U': '55',
'V': '56',
'W': '57',
'X': '58',
'Y': '59',
'Z': '5a',
'[': '5b',
']': '5d',
'^': '5e',
'_': '5f',
'a': '61',
'b': '62',
'c': '63',
'd': '64',
'e': '65',
'f': '66',
'g': '67',
'h': '68',
'i': '69',
'j': '6a',
'k': '6b',
'l': '6c',
'm': '6d',
'n': '6e',
'o': '6f',
'p': '70',
'q': '71',
'r': '72',
's': '73',
't': '74',
'u': '75',
'v': '76',
'w': '77',
'x': '78',
'y': '79',
'z': '7a',
'{': '7b',
'|': '7c',
'}': '7d',
'~': '7e',
' ': '20'
}

