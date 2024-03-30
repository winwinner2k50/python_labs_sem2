import numpy as np
from math import *
def func(func_str, x):
    y = 0
    try:
        y = eval(func_str[func_str.index("=") + 1:])
        return y
    except NameError:
        return "error"
    except ValueError:
        return "error"


def find_root(func_str, a, b, eps, max_eps):
    new = 0
    start_a_b = [a, b]
    for i in range(0, max_eps):
        if((func(func_str, b) - func(func_str, a)) == 0):
            return [start_a_b, 0, 0, i + 1, 2]
        
        new = b - func(func_str, b) * (b - a) / (func(func_str, b) - func(func_str, a))

        if abs(new - a) < eps:
            if new < start_a_b[0] or new > start_a_b[1]:
                return [start_a_b, new, func(func_str, new), i + 1, 3]
            return [start_a_b, new, func(func_str, new), i + 1, 0]
        
        a = b
        b = new
    print("ok")
    return [start_a_b, 0, 0, -1, 1]

def gen_roots(func_str, a, b, h, eps, max_eps):
    roots = []
    x = a
    while(x + h < (b + h / 2)):
        if func(func_str, x) * func(func_str, x + h) <= 0:
            roots.append(find_root(func_str, x, x + h, eps, max_eps))
        x += h

    return roots
    
    
def gen_point(x, y):
    points_x = []
    points_y = []
    for i in range(1, len(y) - 1):
        if (y[i - 1] < y[i] > y[i + 1]) or (y[i - 1] > y[i] < y[i + 1]):
            points_x.append(x[i])
            points_y.append(y[i])
    return points_x, points_y

