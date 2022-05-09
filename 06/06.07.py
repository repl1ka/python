a = int(input('Левая граница:'))
b = int(input('Правая граница:'))
i = 0
summa = 0
n = 0
while (a+i) <= b:
    if ((a+i) % 3) == 0:
        n = n + 1
        summa = summa + (a+i)
    i = i + 1
print(summa/n)