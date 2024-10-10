from Crypto.Util.number import *


u = "HELLO"

data = [ord(char) for char in u]

print(data)

hexx = ''.join(format(x, "02x") for x in data)

print(hexx)

res = int(hexx, 16)

print(res)

longi = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

result = long_to_bytes(longi)

print(result)