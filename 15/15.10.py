string = input('Строка: ')
tpl = input('Кортеж чисел: ')[1:-1].split(', ')

gen = (s for s in zip(string, tpl))

gen_l = list(gen)
print(gen)
i = 0
while(i < len(gen_l)):
    print(gen_l[i])
    i = i + 1
