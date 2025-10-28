# rangeの値を（分母を）大きくしていきe==1になったら処理を終了させる、どの段階で１になるかを確かめためにmachine という変数に＋＝１で１ループするごとに１足していく

machine = 0
e = 0
for i in range(100):
  if e != 0:
        e = 1 / i
        machine += 1
print(machine)


