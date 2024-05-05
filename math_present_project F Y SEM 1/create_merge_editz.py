import numpy as np
import scipy as sp
import sympy as smp
import matplotlib.pyplot as plt
from scipy.misc import derivative

x,y=smp.symbols('x y',real=True)
f=x**3+3*x*y**2-3*x**2-3*y**2+4
# f=(input("Give equation in form of ax**3+b*x*y**2+c*x**2+d*y**2+e\n"))
# print(f)
def run():
    
    x=smp.symbols('x',real=True)
    dfdx=smp.diff(f,x) #first der)ivative wrt x # here we want to keep y contant which is not applicable here
    y=smp.symbols('y',real=True)
    dfdy=smp.diff(f,y) #first der)ivative wrt y # here we want to keep x contant which is not applicable here
    print("Derivative wrt x is ",dfdx)
    print("Derivative wrt y is ",dfdy)
    # return "This is first derivative wrt x and y respectively"

    x=smp.symbols('x',real=True)
    d2fx2=smp.diff(f,x,2) #second derivative wrt x
    y=smp.symbols('y',real=True)
    d2fy2=smp.diff(f,y,2) #second derivative wrt y
    print("Second Derivative wrt x is ",d2fx2)
    print("Second Derivative wrt x is ",d2fy2)
    # return "This are second derivative of x and y respectively"


    x=smp.symbols('x',real=True)
    d2fdxdy=smp.diff(f,x,y) # finding derivative wrt y of dfdy i.e. d2f/dxdy
    y=smp.symbols('y',real=True)
    d2fdydx=smp.diff(f,y,x) # finding derivative wrt y of dfdx i.e. d2f/dydx
    print("Derivative wrt x is ",d2fdxdy)
    print("Derivative wrt y is ",d2fdydx)

    


    # print(dfdx.subs([(x,),(y,)]).evalf())     # evalf() for printing floart value 
    # print(dfdy.subs([(y,),(x,)]).evalf())
    # print("Values had successfully substituted")

    #a= #value if first obtained bracket which will be inserted in place of x 
    #b= #value if first obtained bracket which will be inserted in place of y
    # We have to update that value later to check another obtained point
    r=d2fx2.subs([(x,a),(y,b)]).evalf()
    s=d2fdxdy.subs([(x,a),(y,b)]).evalf()
    t=d2fy2.subs([(x,a),(y,b)]).evalf()

    if r*t-s**2>0 and r<0:
        print("Function is Maximum")
    elif r*t-s**2>0 and r>0:
        print("Function is Minimum")
    elif r*t-s**2<0:
        print("Function is neither maximum nor minimum")
    else:
        print("There is an error")
run()


#------------------------------------------X-----------------------------------------------






# below is for displaying the graph which can done later





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

