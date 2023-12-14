import matplotlib.pyplot as plt
from sympy import symbols, lambdify
from scipy.interpolate import interp1d

euler_t = []
euler_q = []

def euler_method(ode_func, t0, q0, tn, h):
    euler_t.append(t0)
    euler_q.append(q0)
    while t0 <= tn :
        qn = q0 + h * ode_func(t0,q0)
        t0 = t0 + h
        q0 = qn  
        euler_t.append(t0)
        euler_q.append(q0)

t = symbols('t')
q = symbols('q')

function = "(12 - (q / (150 * 10**-6))) / 100"
ode_func = lambdify((t, q), function, 'numpy')
t0 = 0
q0 = 0
tn = 0.005

euler_method(ode_func, t0, q0, tn, tn / 5)

plt.figure(figsize=(8, 6))
plt.plot(euler_t, euler_q, label='Euler Method', color='red')
plt.xlabel('Time')
plt.ylabel('Charge')
plt.legend()
plt.grid(True)
plt.show()

euler_interpolation = interp1d(euler_t, euler_q, kind='linear', fill_value="extrapolate")
euler_qn = euler_interpolation(tn)
print("The estimated value of q at by Eulers method " , tn , " is " , euler_qn)
