from pwn import xor

b = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
data = bytes.fromhex(b)

for i in range(0,255,1):
    res = xor(data, chr(i))
    print(res)