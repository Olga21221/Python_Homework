## Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
## Сколько журавликов сделал каждый ребенок, если известно, 
## что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

sum = int(input('Введите число: '))
a = sum // 6
b = a*4 
print(f"Петя {a}, Катя {b}, Сережа {a}")