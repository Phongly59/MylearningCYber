import base64

u = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

data = bytes.fromhex(u)

result = base64.b64encode(data)

print(result)