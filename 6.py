# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

str_number = input("Введите номер билета: ")
number_len = len(str_number)
if len(str_number) != 6:
    print("Номер должен быть шестизначным")
else:
    number = int(str_number)
    sum = 0
    i = 0
    half_len = number_len / 2
    while number > 0:
        i += 1
        number_right = number % 10
        number //= 10
        if i <= half_len:
            sum += number_right
        else: 
            sum -= number_right
    if sum == 0:    
        print("yes")
    else:
        print("no")

