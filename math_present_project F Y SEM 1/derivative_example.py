import numpy as np
import scipy as sp
import sympy as smp
import matplotlib.pyplot as plt
from scipy.misc import derivative


x,a,b,c=smp.symbols('x a b c',real=True)
f=x**2+1
# print(f)

dfdx=smp.diff(f,x) #first degree derivative
# print(dfdx)

d4fdx4=smp.diff(f,x,4) #forth degree derivative
# print(d4fdx4)

dfdx.subs([(x,4),(a,1),(b,2),(c,3)]).evalf() #putting value respectively and evalf() to get float value
print(dfdx.subs([(x,4),(a,1),(b,2),(c,3)]).evalf())


dfdx_f=smp.lambdify((x,a,b,c),dfdx) #convert numeric function for plotting 
# print(dfdx_f)


x=np.linspace(1,2,100) #define x and y array using hte numerical function above
# print(x)
y=dfdx_f(x,a=1,b=2,c=3)
# print(y)

#plotting of points on graph
# plt.plot(x,y)
# plt.ylabel('$d^4 f/ dx^4$', fontsize=24)
# plt.xlabel('$*$', fontsize=24)



