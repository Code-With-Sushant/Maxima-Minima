
import scipy as s
def f(math):
    x , y = math
    return x**2 + y**2 + 2*x - 4*y +10
guess=[-1,2]
r=s.optimize.minimize(f,guess)
print(r.fun)
print(r.x)
