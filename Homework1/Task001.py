## Задача 2: Найдите сумму цифр трехзначного числа.
a = int(input('Ведите число: '))
sum = 0
sum = (a % 10) + (a // 100) + ((a%100)//10)
print(sum)