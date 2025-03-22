# Derivar f(x) = (2x + 1)^3

from sympy import symbols, diff, ln, sqrt, E, sin

x = symbols("x")
f = (2*x + 1)**3
f_dx = diff(f)
print(f"a) Función original: {f} \n Función derivada: {f_dx}")

f = (x**3 - 3*x**2 + 1)**(-3)
f_dx = diff(f)
print(f"b) Función original: {f} \n Función derivada: {f_dx}")

f = (x - 1/(x**2))**5
f_dx = diff(f)
print(f"c) Función original: {f} \n Función derivada: {f_dx}")

f = ln(x**2)
f_dx = diff(f)
print(f"d) Función original: {f} \n Función derivada: {f_dx}")

f = E**(sqrt(x))
f_dx = diff(f)
print(f"e) Función original: {f} \n Función derivada: {f_dx}")

f = sqrt(ln(sin(x)))
f_dx = diff(f)
print(f"f) Función original: {f} \n Función derivada: {f_dx}")