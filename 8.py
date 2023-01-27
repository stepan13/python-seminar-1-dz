# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Длина шоколадки: "))
m = int(input("Ширина шоколадки: "))
k = int(input("Количество долек на отлом: "))
rows_need = 0
if k % n == 0:
    rows_need = k / n
    rows_all = m
elif k % m == 0:
    rows_need = k / m
    rows_all = n
else:
    rows_all = -1

if rows_need <= rows_all:
    print("yes")
else:
    print("no")
