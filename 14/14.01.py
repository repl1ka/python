number_flt = float(input("Введите своё число:"))
i = 0
if(number_flt> 1):
    while(number_flt > 10):
        number_flt = number_flt/10
        i = i + 1
    print(number_flt, "* 10 **", i)
else:
    while(number_flt < 1):
        number_flt = number_flt*10
        i = i + 1
    print(number_flt, "* 10 **", -i)