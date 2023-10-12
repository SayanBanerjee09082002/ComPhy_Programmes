from sympy import symbols, lambdify
import random

def monte_carlo_method(function, a, b, maxtrials):
    integral = 0.0
    for _ in range(maxtrials):
        integral += function(random.uniform(a,b))
    return integral*((b-a)/(maxtrials-1))

x = symbols('x')

input_expr = input("Enter the function f(x): ")
function = lambdify(x, input_expr, 'numpy')

a = float(input("Enter the lower limit a: "))
b = float(input("Enter the upper limit b: "))
maxtrials = int(input("Set maximum number of trials: "))

print("The solution of the integral is = ", monte_carlo_method(function, a, b, maxtrials))
