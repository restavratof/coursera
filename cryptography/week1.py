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

print('5','-'*30)  # The
print(f'7: result  : {codecs.encode(xor(xor(codecs.decode("6c73d5240a948c86981bc294814d", "hex"), "attack at dawn".encode()), "attack at dusk".encode()), "hex")}')

# >>>'6c73d5240a948c86981bc2808548'
