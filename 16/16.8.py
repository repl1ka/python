nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]

def nice_func (par):
    i = 0
    ret = []
    while i < len(par):
        if type(par[i]) == list:
            if type(par[i][0]) == int:
                ret = ret + par[i]
                i = i + 1
                continue
            else:
                if type(nice_func(par[i])[0]) == int:
                    ret = ret + nice_func(par[i])
                    i = i + 1
                    continue
                else:
                    ret = ret + nice_func(par[i])[0]
                    i = i + 1
                    continue
        else:
            ret.append(par[i])
            i = i + 1
            continue
    return ret
print(nice_func(nice_list))