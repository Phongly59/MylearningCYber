stri = "label"

key = 13

ls = []
for char in stri:
    asci = ord(char)

    res = asci ^ key

    result = chr(res)

    ls.append(result)


new_string = ''.join(ls)


print(new_string)
