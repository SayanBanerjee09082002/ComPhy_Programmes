import matplotlib.pyplot as plt
from sympy import symbols, lambdify
from scipy.interpolate import interp1d

euler_x = []
euler_y = []

def euler_method(ode_func, x0, y0, xn, h):
    euler_x.append(x0)
    euler_y.append(y0)
    while x0 <= xn :
        yn = y0 + h * ode_func(x0,y0)
        x0 = x0 + h
        y0 = yn  
        euler_x.append(x0)
        euler_y.append(y0)

x = symbols('x')
y= symbols('y')

function = input("Enter the function f(x, y) for dy/dx: ")
ode_func = lambdify((x, y), function, 'numpy')
x0 = float(input("Enter the starting value of x: "))
y0 = float(input("Enter the initial value of y: "))
xn = float(input("Enter the ending value of x: "))
h = float(input("Enter the step size: "))

euler_method(ode_func, x0, y0, xn, h)

plt.figure(figsize=(8, 6))
plt.plot(euler_x, euler_y, label='Euler Method', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

euler_interpolation = interp1d(euler_x, euler_y, kind='linear', fill_value="extrapolate")
euler_yn = euler_interpolation(xn)
print("The estimated value of y at by Eulers method " , xn , " is " , euler_yn)
