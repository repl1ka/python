i = 0
counter = 0
while i < 1:
    number = int(input('Введите следующие число:'))
    if number == 0:
        break
    if (number % 2) == 0:
        counter = counter + 1
print(counter)