Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> from scipy import integrate
from numpy import *
from math import *


def fun(x):
    return x / (sqrt(12*x + 0.5))

def rt_int(rectangl, a, b, n):
    h = (b - a) / n
    rt = h * ((fun(a)+h/2) + (fun(b - h)+h/2))
    for i in range(1, n - 1):
        rt += fun(a + i * h)/10
    return rt
  
def rtright_int(fun, a, b, n):
    h = (b - a) / n
    rtright = h * (fun(a) + fun(b - h))
    for i in range(2, n):
        rtright += fun(a + i * h) / 10
    return rtright

def rtleft_int(fun, a, b, n):
    h = (b - a) / n
    rtleft = h * (fun(a) + fun(b - h))
    for i in range(1, n-1):
        rtleft += fun(a + i * h) / 10
    return rtleft
 
a, err = integrate.quad(fun, 0.6, 1.4)


def fun1(x):
    return (math.sin(x**2-1) / 2*sqrt(x))*x
  
def sp_int(fun1, a, b, n):
    h = (b - a) / n
    k = 0.0
    x = a + h
    for i in range(1, n // 2 + 1):
        k += 4 * fun1(x)
        x += 2 * h

    x = a + 2 * h
    for i in range(1, n // 2):
        k += 2 * fun1(x)
        x += 2 * h
    return (h / 3) * (fun1(a) + fun1(b) + k)

b, err = integrate.quad(fun1, 1.3, 2.1)


def fun2(x):
    return x/sqrt(1+2*x**2)

def tr_int(fun2, a, b, n):
    h = (b - a) / n
    sum = 0.5 * (fun2(a) + fun2(b))
    for i in range(1, n):
        sum += fun2(a + i * h)
    return sum * h
  
c, err = integrate.quad(fun2, 0.6, 1.5)


print("middle rectangle method = ", rt_int(fun, 0.6, 1.4, 10))
print("left rectangle method = ", rtleft_int(fun, 0.6, 1.4, 10))
print("right rectangle method = ", rtright_int(fun, 0.6, 1.4, 10))
print('Check for the rectangle method = ', a)

print("Trapezoid method = ", tr_int(fun2, 0.6, 1.5, 20))
print('Check for trapezoid method = ', c)

print("Simpson method= ", sp_int(fun1, 1.3, 2.1, 8))
print('Check for simpson method= ', b)

