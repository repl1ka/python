i = 0
quantity = int(input('Сколько должников у МирПрогБанк?'))
list = range(0, quantity, 5)
arr=[]
sum = 0
counter = 0
for i in list:
    print('Сколько рублей нам должен ', list[counter] ,'-тый:')
    arr.insert(i, int(input()))
    sum = sum+arr[counter]
    counter = counter + 1
print('Опрошенные в сумме должны нам', sum,'рублей.')