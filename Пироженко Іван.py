"lab #14"
from numpy import *
from math import *
import matplotlib.pyplot as plt

def fun1(x, y):
    return x + math.sin(y/1.25)

def fun2(x, y):
    return x + math.cos(y/sqrt(1.3))

def euler(fun1, x, y):
    h = 0.1
    x = 0.5
    y = 1.8
    xarr = ([])
    yarr = ([])
    for i in range (0, 10):
        x += h
        xarr.append([x])
        y += h* fun1(x, y)
        yarr.append([y])
    plt.plot(xarr, yarr)
    plt.title("Lb14")
    plt.xlabel('х')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    return xarr, yarr

def euler_coshi(fun2, x, y):
    h = 0.1
    x = 1.2
    y = 1.8
    xarr = ([])
    yarr = ([])
    for i in range (0, 10):
        x += h
        xarr.append([x])
       
        y += h/2 * (fun2(x, y) + fun2(x+h, fun2(x, y)))
        yarr.append([y])
    plt.plot(xarr, yarr)
    plt.title("lb14")
    plt.xlabel('х')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    return xarr, yarr

print(euler(fun1, 0.5, 1.8))
print(euler_coshi(fun2, 1.2, 2.2))

  





