# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали 
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# S = int(input('Введите количество журавликов '))
# print(int(S / 6), int(S * 2 / 3), int(S / 6))
S = int(input('Введите количество журавликов '))
M=int(str(S))//6
print('Петя = ', M, ', Катя = ', M*4, ', Сережа = ', M)