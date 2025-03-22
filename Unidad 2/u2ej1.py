"""
Graficar la función f(x) = 3x^2 + 1
y su función derivada.
¿Cuál es la pendiente en x = 3?
"""

import sympy as sp

x = sp.symbols("x")
f = 3*x**2 + 1
f_dx = sp.diff(f) # Derivado f
graf = sp.plot(f, show=False) # Gráfico de f
graf_dx = sp.plot(f_dx, show=False) # Gráfico de f'

print(f"La pendiente de f en x = 3 es {f_dx.subs(x, 3)}")

# Esto es para mostrar las dos gráficas en un solo plano
graf.append(graf_dx[0])
graf.show()