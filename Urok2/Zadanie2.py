# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает 
# две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные 
# Петей числа.

S = int(input('Введите сумму чисел '))
P = int(input('Введите произведение чисел '))
for X in range(S):
    for Y in range(P):
        if S == X + Y and P == X * Y:
            print(f'Задуманные числа: X = {X} , Y = {Y}')