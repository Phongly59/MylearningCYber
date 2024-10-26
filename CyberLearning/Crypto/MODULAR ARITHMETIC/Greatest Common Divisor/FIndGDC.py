def GDC(a,b):
    while a != b :
        if (a > b ):
            a = a -b
        else:
            b = b -a
    
    return a


a = 26513
b = 32321
print(GDC(a,b))