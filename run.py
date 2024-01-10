from apnum.num import Num


print(Num(123))
print(Num(123, 234))
print(Num(1.23, 23.4))
print(Num(123000, 2340))
print(Num(123000, 2340) + Num(123000, 2340))
print(Num(123001, 2342) - Num(123000, 2340))
