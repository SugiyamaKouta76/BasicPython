a = 14
b = 91
# TODO]
q = 0
r = 0
if a >= b:
    q = a // b
    r = a - (q * b)
else:
    q = b // a
    r = b - (q * a)
print(q,r)

while r != 0:
    if a >= b:
        a = q
        b = r
        q = a // b
        r = a - (q * b)
    else:
        b = q
        a = r
        q = b // a
        r = b - (q * a)
print(q,r)




    

        


