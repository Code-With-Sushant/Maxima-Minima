import pyautogui
import time
import scipy as sp
time.sleep(10)
cout=0
while cout<=10:
    pyautogui.typewrite('''My Love❤️❤️❤️''')
    pyautogui.press("")
    cout+=1
def f(math):
    x , y = math
    return x**2 + y**2 + 2*x - 4*y +10
guess=[-1,2]
r=sp.optimize.minimize(f,guess)
print(r.fun)
print(r.x)