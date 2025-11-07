# rangeの値を（分母を）大きくしていきe==1になったら処理を終了させる、どの段階で１になるかを確かめためにmachine という変数に＋＝１で１ループする
e = 1
a = 0
number = 1 + e

for i in range(100):
    if number != 1:
        e = 1 / (2 ** i)
        number = 1 + e
        a += 1

b = 1 / (2 ** a)
print(e)



