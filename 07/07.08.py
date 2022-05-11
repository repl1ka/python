N = int(input('До какого члена считаем наш ряд? '))
sum = 1
current_number = 0
for i in range(1,N, 1):
    current_number = ((-1)**i)/(2**i)
    sum = sum + current_number
print(sum)