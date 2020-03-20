
raw_str = 'Hello World!'
raw_bytes = raw_str.encode()
print(f'ASCII -> Raw Bytes   : {raw_bytes}')
hex_val = raw_bytes.hex()
print(f'Raw Bytes -> HEX     : {hex_val}')
ascii_val = raw_bytes.decode()
print(f'Raw Bytes -> ASCII   : {ascii_val}')
# Convert Random RAW Bytes to ASCII string - This cannot be done! Random RAW Bytes do not correspond to ascii or utf-8 codes.
ch_val = 'A'
ord_val = ord(ch_val)
print(f'Char -> ASCII code   : {ord_val}')
print(f'ASCII code -> Char   : {chr(ord_val)}')
int_bytes_val = bytes([200])
print(f'INT (0,256) -> Raw Bytes : {int_bytes_val}')
print(f'Raw Bytes -> INT     : {int(int_bytes_val.hex(),16)}')
print(f'Raw Bytes -> INT     : {ord(int_bytes_val)}')
hex_val = hex(200)
print(f'INT -> Hex           : {hex_val}')
print(f'Hex -> INT           : {0xc8}')   # automatic
print(f'Decimal INT -> Binary: {bin(200)}')
print(f'Binary -> Decimal INT: {0b11001000}')


# ASCII -> Raw Bytes   : b'Hello World!'
# Raw Bytes -> HEX     : 48656c6c6f20576f726c6421
# Raw Bytes -> ASCII   : Hello World!
# Char -> ASCII code   : 65
# ASCII code -> Char   : A
# INT (0,256) -> Raw Bytes : b'\xc8'
# Raw Bytes -> INT     : 200
# Raw Bytes -> INT     : 200
# INT -> Hex           : 0xc8
# Hex -> INT           : 200
# Decimal INT -> Binary: 0b11001000
# Binary -> Decimal INT: 200



