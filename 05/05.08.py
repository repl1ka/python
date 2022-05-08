contribution = int(input('Cумма вклада:'))
procent = int(input('Процент:'))
Y = int(input('Сколько денег хотим?'))
i = 0
summa = contribution
while summa < Y:
    summa = summa * (1 + procent/100)
    summa = int(summa)
    i = i + 1
print(i)