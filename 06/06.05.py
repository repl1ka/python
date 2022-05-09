n = int(input('Введите число, факториал которого вам нужен:'))
i = 1
fac = 1
while i <= n:
    fac = fac * i
    i = i + 1
print(fac)