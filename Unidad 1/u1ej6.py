"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""

clave = "contraseña"
entrada = input("Ingrese la contraseña: ")
while clave != entrada:
    entrada = input("Contraseña incorrecta. Intente de nuevo: ")
print("Contraseña correcta")