a = int(input('Введите левую границу:'))
b = int(input('Введите правую границу:'))
c = int(input('Среднее арифметическое всех чисел от a до b, кратных - '))
sum = 0
counter = 0
for i in range(a,b+1,1):
    if i%c == 0:
        sum = sum+i
        counter=counter+1
print(sum/counter)
