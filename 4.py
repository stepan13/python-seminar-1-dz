# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

all = int(input("Всего журавликов: "))
if all % 6 == 0:
    part = round(all / 6)
    print(f"Петя: {part}, Катя: {4*part}, Сережа: {part}")
else:
    print(f"Невозможно по условию задачи столько журавликов: {all}")
