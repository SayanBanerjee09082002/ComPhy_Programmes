import matplotlib.pyplot as plt
from sympy import symbols, lambdify
from scipy.interpolate import interp1d

euler_x = []
euler_y = []
modified_euler_x = []
modified_euler_y = []
improved_euler_x = []
improved_euler_y = []
runge_kutta_x = []
runge_kutta_y = []

def euler_method(ode_func, x0, y0, xn, h):
    euler_x.append(x0)
    euler_y.append(y0)
    while x0 <= xn :
        yn = y0 + h * ode_func(x0,y0)
        x0 = x0 + h
        y0 = yn  
        euler_x.append(x0)
        euler_y.append(y0) 

def modified_euler_method(ode_func, x0, y0, xn, h):
    modified_euler_x.append(x0)
    modified_euler_y.append(y0)
    while x0 <= xn :
        f = ode_func(x0,y0)
        yn = y0 + h * ode_func(x0 + (h / 2), y0 + ((h * f) / 2))
        x0 = x0 + h
        y0 = yn  
        modified_euler_x.append(x0)
        modified_euler_y.append(y0) 

def improved_euler_method(ode_func, x0, y0, xn, h):
    improved_euler_x.append(x0)
    improved_euler_y.append(y0)
    while x0 <= xn:
        f = y0 + h * ode_func(x0, y0)
        yn = y0 + 0.5 * h * (ode_func(x0, y0) + ode_func(x0 + h, f))
        x0 = x0 + h
        y0 = yn
        improved_euler_x.append(x0)
        improved_euler_y.append(y0)

def runge_kutta_method(ode_func, x0, y0, xn, h):
    runge_kutta_x.append(x0)
    runge_kutta_y.append(y0)
    while x0 <= xn:
        k1 = h * (ode_func(x0, y0))
        k2 = h * (ode_func((x0 + h / 2), (y0 + k1 / 2)))
        k3 = h * (ode_func((x0 + h / 2), (y0 + k2 / 2)))
        k4 = h * (ode_func((x0 + h), (y0 + k3)))
        yn = y0 + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x0 = x0 + h
        y0 = yn
        runge_kutta_x.append(x0)
        runge_kutta_y.append(y0)

x = symbols('x')
y = symbols('y')

function = input("Enter the function f(x, y) for dy/dx: ")
ode_func = lambdify((x, y), function, 'numpy')
x0 = float(input("Enter the starting value of x: "))
y0 = float(input("Enter the initial value of y: "))
xn = float(input("Enter the ending value of x: "))
h = float(input("Enter the step size: "))

euler_method(ode_func, x0, y0, xn, h)
modified_euler_method(ode_func, x0, y0, xn, h)
improved_euler_method(ode_func, x0, y0, xn, h)
runge_kutta_method(ode_func, x0, y0, xn, h)

plt.figure(figsize=(8, 6))
plt.plot(euler_x, euler_y, label='Euler Method', color='blue')
plt.plot(modified_euler_x, modified_euler_y, label='Modified Euler Method', color='green')
plt.plot(improved_euler_x, improved_euler_y, label='Improved Euler Method', color='orange')
plt.plot(runge_kutta_x, runge_kutta_y, label='Runge Kutta Method', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

euler_interpolation = interp1d(euler_x, euler_y, kind='linear', fill_value="extrapolate")
euler_yn = euler_interpolation(xn)
print("The estimated value of y at by Eulers method " , xn , " is " , euler_yn)

modified_euler_interpolation = interp1d(modified_euler_x, modified_euler_y, kind='linear', fill_value="extrapolate")
modified_euler_yn = modified_euler_interpolation(xn)
print("The estimated value of y at by Modified Eulers method " , xn , " is " , modified_euler_yn)

improved_euler_interpolation = interp1d(improved_euler_x, improved_euler_y, kind='linear', fill_value="extrapolate")
improved_euler_yn = improved_euler_interpolation(xn)
print(f"The estimated value of y at by Improved Euler method  " , xn , " is " , improved_euler_yn)

runge_kutta_interpolation = interp1d(runge_kutta_x, runge_kutta_y, kind='linear', fill_value="extrapolate")
runge_kutta_yn = runge_kutta_interpolation(xn)
print(f"The estimated value of y at by Runge Kutta method  " , xn , " is " , runge_kutta_yn)

