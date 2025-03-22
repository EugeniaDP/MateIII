"""
Escribir un programa que pida al usuario dos números enteros (n y m) y muestre en pantalla: "La 
división entera entre n y m da un cociente c y un resto r" Donde n y m son los números 
introducidos por el usuario, y c y r son el cociente y el resto de la división entera 
respectivamente.
"""

n = int(input("Ingrese un número entero: "))
m = int(input("Ingrese otro número entero: "))
c = n // m
r = n % m
print(f"La división entera entre {n} y {m} da un cociente de {c} y un resto de {r}")