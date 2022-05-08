number = int(input('Введите шестизначное число:'))
left = number//100000 + (number//10000)%10 + (number//1000)%10
right = (number//100)%10 + (number//10)%10 + number%10
if left == right:
    print('Вы счастливчик!')
else:
    print('Повезёт на обратном пути!')