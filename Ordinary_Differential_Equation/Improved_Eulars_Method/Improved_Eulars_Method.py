import matplotlib.pyplot as plt
from sympy import symbols, lambdify
from scipy.interpolate import interp1d

improved_euler_x = []
improved_euler_y = []

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

x = symbols('x')
y= symbols('y')

function = input("Enter the function f(x, y) for dy/dx: ")
ode_func = lambdify((x, y), function, 'numpy')
x0 = float(input("Enter the starting value of x: "))
y0 = float(input("Enter the initial value of y: "))
xn = float(input("Enter the ending value of x: "))
h = float(input("Enter the step size: "))

improved_euler_method(ode_func, x0, y0, xn, h)

plt.figure(figsize=(8, 6))
plt.plot(improved_euler_x, improved_euler_y, label='Improved Euler Method', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

improved_euler_interpolation = interp1d(improved_euler_x, improved_euler_y, kind='linear', fill_value="extrapolate")
improved_euler_yn = improved_euler_interpolation(xn)
print(f"The estimated value of y at by Improved Euler method " , xn , " is " , improved_euler_yn)
