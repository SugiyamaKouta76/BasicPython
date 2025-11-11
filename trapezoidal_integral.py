#わからない
import math as mt
# --example--
# print(sin(0))
# >>> 0
# -----------
a = 0
b = (mt.pi/2)
int(b)
n = 100
h = (b - a) / n

for i in range(a,b):
    size = (mt.sin(i) + mt.sin(i + h)) / 2 * h
    print(size)

