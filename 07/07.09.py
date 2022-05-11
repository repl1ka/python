x = int(input('Введите число Х:'))
numerator = 1
denominator = 1
for i in range(1, 65, 1):
    if i%2 == 0:
        denominator = denominator*(x-i)
    else:
        numerator = numerator*(x-i)
print(numerator/denominator)