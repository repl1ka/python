a = input('Введите последовательность чисел:')
a = a.split()
i = 0
flag = 0
while i < 9:
    if int(a[i+1]) > int(a[i]):
        i = i + 1
        continue
    else:
        print('Начальство вас не ценит, время менять работу!')
        flag = 1
        break
if flag == 0:
    print('Поздравляем! У вас прекрасное место работы.')