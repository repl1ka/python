import random
r = random.randint(1,10)
i = 0
counter = 0
while i < 1:
    user_number = int(input('Введите число:'))
    if user_number > r:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
    elif user_number < r:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
    else:
        print('Вы угадали! Число попыток:', (counter + 1))
        break
    counter = counter + 1