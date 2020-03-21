import codecs

# SOURCES:
# https://crypto.stackexchange.com/questions/33673/many-time-pad-attack-xor
# https://cryptopals.com/

separator = '-'*100
#--------------------------------------------------------------------------------
# Part 1: Bob -> Eve
#--------------------------------------------------------------------------------
print('1',separator)
print('  - Part 1: Bob -> Eve')

def xor(a, b):
    return bytes(x^y for x, y in zip(a, b))

print(xor(b'Bob', b'Eve').hex())
# >> '071907'

#--------------------------------------------------------------------------------
# Part 2: Dawn -> Dusk
#--------------------------------------------------------------------------------
print('2',separator)
print('  - Part 2: Dawn -> Dusk')

ct = "6c73d5240a948c86981bc294814d"
orig_text = 'attack at dawn'
new_text = 'attack at dusk'

def strxor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

c = codecs.decode(ct, 'hex')
print(f"   c(enc): {c}")
m1 = orig_text.encode()
print(f" m1 (enc): {m1}")
m2 = new_text.encode()
print(f" m2 (enc): {m2}")
r1 = xor(c, m1)
print(f"         : {r1}")
r2 = xor(r1, m2)
print(f"         : {r2}")
result = codecs.encode(r2, 'hex')
print(f" result 1: {result}")
# >>>'6c73d5240a948c86981bc2808548'
print(f' result 2: {codecs.encode(xor(xor(codecs.decode(ct, "hex"), orig_text.encode()), new_text.encode()), "hex")}')
# >>>'6c73d5240a948c86981bc2808548'

#--------------------------------------------------------------------------------
# TEST
#--------------------------------------------------------------------------------
print('3',separator)
print('  - Part 3: ')
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


