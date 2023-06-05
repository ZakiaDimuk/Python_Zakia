# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# 1 Вариант
# n = int(input('Введите кол-во элементов первого множества: '))
# m = int(input('Введите кол-во элементов второго множества: '))
# elements1 = set()

# for i in range(n):
#     num = input()
#     elements1.add(num)
# print(elements1)

# elements2 = set()
# for i in range(m):
#     num = input()
#     elements2.add(num)
# print(elements2)

# p = sorted(elements1.intersection(elements2))
# print(*p)

# 2 Вариант

# from random import randint

# n = set(randint(1, 15) for i in range(int(input('Введите кол-во элементов первого множества: '))))
# print(n)
# m = set(randint(1, 15) for i in range(int(input('Введите кол-во элементов второго множества: '))))
# print(m)

# p = sorted(n.intersection(m))
# print(*p)