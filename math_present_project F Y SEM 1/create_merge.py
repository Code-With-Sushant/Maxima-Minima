import numpy as np
import scipy as sp
import sympy as smp
import matplotlib.pyplot as plt
from scipy.misc import derivative
from sympy import *

x,y=smp.symbols('x y',real=True)
f=x**3+3*x*y**2-3*x**2-3*y**2+4
# f=sympify(input("Give equation in form of ax**3+b*x*y**2+c*x**2+d*y**2+e\n"))
# print(f)
def fd():
    dfdx=smp.diff(f,x) #first der)ivative wrt x
    dfdy=smp.diff(f,y) #first der)ivative wrt y
    print("Derivative wrt x is ",dfdx)
    print("Derivative wrt y is ",dfdy)
    # return "This is first derivative wrt x and y respectively"

def sd():
    d2fx2=smp.diff(f,x,2) #second derivative wrt x
    d2fy2=smp.diff(f,y,2) #second derivative wrt y
    print("Second Derivative wrt x is ",d2fx2)
    print("Second Derivative wrt x is ",d2fy2)
    # return "This are second derivative of x and y respectively"

def md():
    dxdt=smp.diff(f,x,t)
    dydt=smp.diff(f,y,t)
    dxdy=dxdt/dydt
    print(dxdy)


def putValues_1():
    print(dfdx.subs([(x,),()]).evalf())
    print(dfdy.subs([(y,),()]).evalf())
    return "Values had successfully entered"

def putValues_2():
    print(d2fx2.subs([(x,),()]).evalf())
    print(d2fy2.subs([(y,),()]).evalf())
    return "Values had successfully entered"

# def put_x_0():
#     # dfdx=0
#     # dfdy=0
#     print(Expr(dfdx))
#     print(Expr(dfdy))
#     return None


calculate_first_d=fd()
calculate_second_d=sd()
# consider_x=put_x_0()
print(calculate_first_d)
print(calculate_second_d)
# print(consider_x)

 
 
 
 
 














# r=
# t=
# s=


# if rt-s**2>0 and r<0:
#     print("Given function is maximum")
# elif rt-s**2>0 and r>0:
#     print("Given function is minimum")
# elif rt-s**2<0:
#     print("Given functiois nither maximum nor minimum")














# dfdx_f=smp.lambdify((x,a,b,c),dfdx) #convert numeric function for plotting 
# print(dfdx_f)


# x=np.linspace(1,2,100) #define x and y array using hte numerical function above
# print(x)
# y=dfdx_f(x,a=1,b=2,c=3)
# print(y)

#plotting of points on graph
# plt.plot(x,y)
# plt.ylabel('$d^4 f/ dx^4$', fontsize=24)
# plt.xlabel('$*$', fontsize=24)

