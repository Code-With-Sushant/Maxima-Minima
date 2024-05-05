# # // write a computer program to compute maxima and minima of function by taking input?
# def my_function():
#     temps = [] ## Empty list to be filled
#     asking = True ## Switch to keep asking
#     while asking:
#         temp=input("Enter temperature:")
#         try:
#             temp=int(temp)
#             temps.append(temp) ## If a number was entered, add it to the list
#         except: ## Stop asking if no number was entered
#             asking = False
#     if len(temps)>0:
#         mean_value=sum(temps)/len(temps)
#         min_value = min(temps)
#         max_value = max(temps)
#         print(mean_value,min_value,max_value)
#     else:
#         print("no numbers were entered")







# // write a computer program for computing maxima and minima of function?
# number = raw_input('Enter number:')
# list_of_numbers = number.split()

# numbersInt = map(int, list_of_numbers) # convert string list to integer list

# print("Size:",    len(numbersInt))
# print("Min:",     min(numbersInt))
# print("Max:",     max(numbersInt))
# print("Sum:",     sum(numbersInt))
# print("Average:", float(sum(numbersInt))/len(numbersInt) if len(numbersInt) > 0 else float('nan'))
# # float conversion is only required by Python 2. 








# // write a computer program to compute maxima and minima of function?

import numpy as np
from numpy.polynomial import Polynomial

def find_extrema(poly, bounds):
    deriv = poly.deriv()
    extrema = deriv.roots()
    # Filter out complex roots
    extrema = extrema[np.isreal(extrema)]
    # Get real part of root
    extrema = np.real(extrema)
    # Apply bounds check
    lb, ub = bounds
    extrema = extrema[(lb <= extrema) & (extrema <= ub)]
    return extrema

def find_minimum(poly, bounds):
    extrema = find_extrema(poly, bounds)
    # Note: initially I tried taking the 2nd derivative to filter out local maxima.
    # This ended up being slower than just evaluating the function.

    # Either bound could end up being the minimum. Check those too.
    extrema = np.concatenate((extrema, bounds))
    # Check every candidate by evaluating the polynomial at each possible minimum,
    # and picking the minimum.
    value_at_extrema = poly(extrema)
    minimum_index = np.argmin(value_at_extrema)
    return extrema[minimum_index]

# Warning: polynomial expects coeffients in the opposite order that you use.
poly = Polynomial([5,1,3,6,4]) 
print(find_minimum(poly, (-5, 5)))


p = np.poly1d([4,6,3,1,5])  # Note: polynomials are opposite order of before

def find_minimum2(poly):
    roots = np.real(np.roots(poly.deriv()))
    return roots[np.argmin(poly(roots))]

print(find_minimum2(p))



# -//find derivative of a fu
# 
# nction by taking function as input?
# from sympy import *
# import numpy as np
# x = Symbol('x')
# y = x**2 + 1
# yprime = y.diff(x)
# print(yprime)





from scipy.misc import derivative
import math
def f(x):
  return math.cos(x)

y1 = derivative(f,5.0,dx=1e-9)


