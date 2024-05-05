
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


// write a computer program to compute maxima and minima of function by taking input?
import sympy as sym
x, y = sym.symbols("x y")
f = sym.cos(x*10)**2 + sym.sin(y*10)**2
gradient = sym.derive_by_array(f, (x, y))
hessian = sym.Matrix(2, 2, sym.derive_by_array(gradient, (x, y)))


stationary_points = sym.solve(gradient, (x, y))
for p in stationary_points:
    value = f.subs({x: p[0], y: p[1]})
    hess = hessian.subs({x: p[0], y: p[1]})
    eigenvals = hess.eigenvals()
    if all(ev > 0 for ev in eigenvals):
        print("Local minimum at {} with value {}".format(p, value))
    elif all(ev < 0 for ev in eigenvals):
        print("Local maximum at {} with value {}".format(p, value))
    elif any(ev > 0 for ev in eigenvals) and any(ev < 0 for ev in eigenvals):
        print("Saddle point at {} with value {}".format(p, value))
    else:
        print("Could not classify the stationary point at {} with value {}".format(p, value))


Saddle point at (0, 0) with value 1
Local maximum at (0, pi/20) with value 2
Saddle point at (0, pi/10) with value 1
Local maximum at (0, 3*pi/20) with value 2
Local minimum at (pi/20, 0) with value 0
Saddle point at (pi/20, pi/20) with value 1
Local minimum at (pi/20, pi/10) with value 0
Saddle point at (pi/20, 3*pi/20) with value 1
Saddle point at (pi/10, 0) with value 1
Local maximum at (pi/10, pi/20) with value 2
Saddle point at (pi/10, pi/10) with value 1
Local maximum at (pi/10, 3*pi/20) with value 2
Local minimum at (3*pi/20, 0) with value 0
Saddle point at (3*pi/20, pi/20) with value 1
Local minimum at (3*pi/20, pi/10) with value 0
Saddle point at (3*pi/20, 3*pi/20) with value 1


from scipy.optimize import fsolve
grad = sym.lambdify((x, y), gradient)
fsolve(lambda v: grad(v[0], v[1]), (1, 2))


