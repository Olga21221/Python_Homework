"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""
x = int(input('Введите число: '))
l = []
for i in range(x):
    l.append(int(input('Введите числа: ')))

y = int(input('Введите сравниваемое число: '))
u=y
a = 0
for i in range(len(l)):
    if y >= l[i]:
        if y - l[i]<u:
            u = y - l[i]
            a = l[i]
    else:
        if l[i] - y<u:
            u = l[i] - y
            a = l[i]
print(a)