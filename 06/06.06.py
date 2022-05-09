a = input('Введите оценки учеников:')
a = a.split()
i = 0
jun = 0
mid = 0
sen = 0
while i < len(a):
    if int(a[i]) == 3:
        jun = jun + 1
    elif int(a[i]) == 4:
        mid = mid + 1
    elif int(a[i]) == 5:
        sen = sen + 1
    i = i + 1
if jun > mid:
    if mid > sen:
        print('Троечников больше всех')
    else:
        if sen > jun:
            print('Отличников больше всех')
        else:
            print('Троечников больше всех')
else:
    if mid > sen:
        print('Золотая середина - идеальный баланс')
    else:
        print('Отличников больше всех')