name = input('Как вас зовут?')
debt = input('Сумма вашего долга?')
debt_int = int(debt)
print(name + ', ваша задолженность составляет ' + debt + ' рублей.')
i = 0
while i < debt_int:
    i = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить?'))
    if i < debt_int:
        print('Маловато, '+ name +'. Давайте ещё раз.')
    else:
        print('Отлично, '+ name +'! Вы погасили долг. Спасибо!')
        break;