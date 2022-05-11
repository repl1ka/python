import random
time_until_explosion = int(input('Сколько времени до взрыва?'))
step = random.randint(0, time_until_explosion)
choice = 0
flag = 0
counter = 1
flag_two = 0
for i in range(0, time_until_explosion, step):
    choice = int(input('Будем обезвреживать бомбу? 0 - нет, 1 - да'))
    if choice == 1:
        print('Бомба обезврежена за', i, 'секунд.')
        flag = 1
        break
    else:
        flag_two = time_until_explosion-counter*step
        if flag_two < 0:
            flag_two = 0
        print('Бомба взорвётся через', flag_two, 'секунд')
    counter = counter + 1
if flag == 0:
    print('Бомба взорвалась, вы померли!')