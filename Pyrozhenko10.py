from numpy import *
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
x = [0.5,0.9,1.5,2.3,3]
y = [1.54,3.38,2.53,1.86,4.35]
spl= UnivariateSpline(x,y)
xs = linspace(0.6,2.2,300)
plt.plot(x,y,'ro',xs,spl(xs),'r')
plt.title('Pyrozhenko Lab10')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

