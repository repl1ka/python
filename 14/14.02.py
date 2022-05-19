def comparison(a,b):
    if a > b:
        return a
    else:
        return b
def super_comparison(a,b,c):
    if comparison(a,b) == comparison(a,c):
        return a
    elif comparison(a,b) == comparison(b,c):
        return b
    else:
        return c
a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
c = int(input("Введите третье число:"))
print(super_comparison(a,b,c))