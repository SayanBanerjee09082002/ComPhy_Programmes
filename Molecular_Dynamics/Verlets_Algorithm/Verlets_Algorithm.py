import matplotlib.pyplot as plt
from sympy import symbols, lambdify

postion = []
velocity = []
time = []

def verlets_algorithm (acceleration_func, x0, v0, t0, tn, dt) :
    postion.append(x0)
    velocity.append(v0)
    time.append(t0)
    
    while (t0 <= tn) :
        x0 = x0 + (v0 * (dt/2))
        v0 = v0 + acceleration_func(x0) * dt
        x0 = x0 + (v0 * (dt/2))
        t0 = t0 + dt
        postion.append(x0)
        velocity.append(v0)
        time.append(t0)

x = symbols('x')
y = symbols('y')

function = input("Enter the function f(x) for acceleration: ")
acceleration_func = lambdify(x, function, 'numpy')
x0 = float(input("Enter initial position: "))
v0 = float(input("Enter initial velocity: "))
dt = float(input("Enter step time: "))
tn = float(input("Enter end time: "))

verlets_algorithm(acceleration_func, x0, v0, 0, tn, dt)

plt.figure(figsize=(8, 6))
plt.plot(time, postion, label='Position', color='blue')
plt.plot(time, velocity, label='Velocity', color='red')
plt.xlabel('Time')
plt.ylabel('Position / Velocity')
plt.legend()
plt.grid(True)
plt.show()