import codecs

# SOURCES:
# https://crypto.stackexchange.com/questions/33673/many-time-pad-attack-xor
# https://cryptopals.com/

separator = '-'*100
#--------------------------------------------------------------------------------
# Part 1: Bob -> Eve
#--------------------------------------------------------------------------------
print('1',separator)
print('-','Part 1: Bob -> Eve')

def xor(a, b):
    return bytes(x^y for x, y in zip(a, b))

print(xor(b'Bob', b'Eve').hex())
# >> '071907'

#--------------------------------------------------------------------------------
# Part 2: Dawn -> Dusk
#--------------------------------------------------------------------------------
print('2',separator)
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

print('3',separator)
print('-','Part 3: ')
# Example:  hex of 'a' = 61  hex of space = 20 XOR 'a' and space = 41 = 'A' (in hex)
# same as:  hex of 'z' = 7A  hex of space = 20 XOR 'z' and space = 5A = 'Z' (in hex)
ch1 = 'a'
ch2 = ' '
xor_out = xor(ch1.encode(), ch2.encode())
print(f'hex of "{ch1}" = {hex(ord(ch1))} hex of "{ch2}" = {hex(ord(ch2))} ; XOR "{ch1}" and "{ch2}" = {hex(ord(xor_out.decode()))} = {xor_out}')
ch1 = 'z'
xor_out = xor(ch1.encode(), ch2.encode())
print(f'hex of "{ch1}" = {hex(ord(ch1))} hex of "{ch2}" = {hex(ord(ch2))} ; XOR "{ch1}" and "{ch2}" = {hex(ord(xor_out.decode()))} = {xor_out}')

print(f"'{ch1}' hex({ch1.encode().hex()}) binary({bin(ord(ch1))})")
#    'a'  hex(61) binary(0b1100001)


print('4',separator)
all_list = [ ' ', '!', '#', '$', '%', '&', '`', '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', ']', '^', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~' ]

for ch in all_list:
    print(f"'{ch}': {hex(ord(ch))} : {ch.encode()} : {xor(ch.encode(), b' ')}")


