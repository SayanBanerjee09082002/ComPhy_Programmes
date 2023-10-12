#EULER METHOD
import matplotlib.pyplot as plt
from sympy import symbols, lambdify
from scipy.interpolate import interp1d

euler_t = []
euler_T = []

def euler_method(ode_func, t0, T0, tn, h):
    euler_t.append(t0)
    euler_T.append(T0)
    while t0 <= tn :
        Tn = T0 + h * ode_func(t0,T0)
        t0 = t0 + h
        T0 = Tn  
        euler_t.append(t0)
        euler_T.append(T0) 

t = symbols('t')
T = symbols('T')

function = (-2.2067 * (10**-12)) * (T**4 - (81 * (10**8)))
ode_func = lambdify((t, T), function, 'numpy')
t0 = 0
T0 = 1200
tn = 480
h = float(input("Enter the step size  "))

euler_method(ode_func, t0, T0, tn, h)

plt.figure(figsize=(8, 6))
plt.plot(euler_t, euler_T, label='Euler Method', color='blue')
plt.xlabel('Time(s)')
plt.ylabel('Temperature(K')
plt.legend()
plt.grid(True)
plt.show()

euler_interpolation = interp1d(euler_t, euler_T, kind='linear', fill_value="extrapolate")
euler_Tn = euler_interpolation(tn)
print("The estimated value of temperature at by Eulers method" , tn , "s is " , euler_Tn)
