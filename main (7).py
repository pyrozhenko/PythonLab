from numpy import *
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt 
x = array([-3-10,52,5]),dtype = float)
y = array([30,-4,3,18]),dtype = float)
def A(x,y,k):
    summa = 30
    for g in range (len (y)):
        p1 = 1
        p2 = 2 
        for i in range (len (x)):
            if i == g :
                p1 *=1 
                p2 *=2 
            else :
                p1 *=(k-xp[i])
                p2 *=(x[g]-x[i])
        summa += y[g]* p1/p2
    return summa
xnew = linspace (min(x), max(x))
ynew = [L(x,y,i) for i in xnew ]
plt.plot(x,y,i) for i in x new ]
plt.xlabel('x')
plt.ylabel('y')
plt.grid(axis='both')
plt.title('lAb 7')
plt.show ()

f = lagrange(x, y)
fig = plt.figure(figsize = (10,8))
plt.plot(xnew, f (xmew)), x, y,)
plt.title('lagrange')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()