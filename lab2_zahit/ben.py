def sum_9(a, b):
    print(a, b)
    if "." not in a:
        a+=".0"
    if "." not in b:
        b+=".0"
    a_float_int = a.split('.')
    b_float_int = b.split('.')
    res_int = sum_9_int(a_float_int[0], b_float_int[0])
    res_float = sum_9_float(a_float_int[1], b_float_int[1])
    print(res_int, res_float)
    if len(res_float) > max(len(a_float_int[1]), len(b_float_int[1])):
        res_int = sum_9_int(res_int, res_float[0])
        res_float = res_float[1:]
    
    return res_int + "." + res_float
#вычисление целой части
def sum_9_int(a, b):
    a = list(map(int, a))[::-1]
    b = list(map(int, b))[::-1]
    if len(a) > len(b):
        b += [0]*(len(a)-len(b))
    else:
        a += [0]*(len(b)-len(a))
    i = 0
    sum_res = list()
    while i < len(a) or i < len(b):
        if a[i] + b[i] < 9:
            if len(sum_res) <= i:
                sum_res.append(a[i] + b[i])
            else:
                if a[i] + b[i] + sum_res[i] < 9:
                    sum_res[i] = a[i] + b[i] + sum_res[i]
                else:
                    sum_res[i] = a[i] + b[i] + sum_res[i] - 9
                    sum_res.append(1)
        else:
            if len(sum_res) <= i: 
                sum_res.append(a[i] + b[i] - 9)
                sum_res.append(1)
            else:
                sum_res[i] += a[i] + b[i] - 9
                sum_res.append(1)
        i += 1

    
    sum_res = list(map(str, sum_res))
    return "".join(sum_res[::-1])

def sum_9_float(a, b):

    a = list(map(int, a))
    b = list(map(int, b))

    if len(a) > len(b):
        b += [0]*(len(a)-len(b))
    else:
        a += [0]*(len(b)-len(a))

    a = a[::-1]
    b = b[::-1]

    i = 0
    sum_res = list()
    while i < len(a) or i < len(b):
        if a[i] + b[i] < 9:
            if len(sum_res) <= i:
                sum_res.append(a[i] + b[i])
            else:
                if a[i] + b[i] + sum_res[i] < 9:
                    sum_res[i] = a[i] + b[i] + sum_res[i]
                else:
                    sum_res[i] = a[i] + b[i] + sum_res[i] - 9
                    sum_res.append(1)
        else:
            if len(sum_res) <= i: 
                sum_res.append(a[i] + b[i] - 9)
                sum_res.append(1)
            else:
                sum_res[i] += a[i] + b[i] - 9
                sum_res.append(1)
        i += 1
    sum_res = list(map(str, sum_res))
    
    return "".join(sum_res[::-1])
