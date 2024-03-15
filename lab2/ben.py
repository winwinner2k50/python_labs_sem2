def func(func_str, x):
    y = 0
    y = eval(func_str[func_str.index("=") + 1:])
    return y


def find_root(func_str, func, a, b, eps, max_eps):
    new = None
    for i in range(0, max_eps):
        new = x1 - func(func_str, b) * (b - a) / (func(func_str, b) - func(func_str, a))

        if abs(new - a) < eps:
            return new
        
        a = b
        b = new
    
    return None

q = input()
x = int(input())
print(func(q, x))
