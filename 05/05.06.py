i = 0
counter_positive = 0
counter_negative = 0
while i < 1:
    number = int(input('Введите следующие число:'))
    if number == 0:
        break
    if number > 0:
        counter_positive = counter_positive + 1
    else:
        counter_negative = counter_negative + 1
print('Кол-во положительных чисел: ', counter_positive)
print('Кол-во отрицательных чисел: ', counter_negative)