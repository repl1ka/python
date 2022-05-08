i = 0
number = 50
left_border = 0
right_border = 100
counter = 0
while i < 1:
    print("Твоё число равно, меньше или больше, чем число", number,'?')
    b = int(input())
    if b == 2:
        left_border = number
        number = (left_border + right_border)//2
    elif b == 3:
        right_border = number
        number = (left_border + right_border)//2
    elif b == 1:
        print('Вы угадали! Число попыток:', (counter + 1))
        break
    counter = counter + 1