"""
 Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los 
clientes se guardarán en un diccionario en el que el key de cada cliente será su CUIT, y el valor 
será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), 
donde preferente tendrá el valor True si se trata de un cliente preferente.
 El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) 
Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, 
(6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:
 • Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de 
datos.
 • Preguntar por el CUIT del cliente y eliminar sus datos de la base de datos.
 • Preguntar por el CUIT del cliente y mostrar sus datos.
 • Mostrar lista de todos los clientes de la base datos con su CUIT y nombre.
 • Mostrar la lista de clientes preferentes de la base de datos con su CUIT y nombre.
 • Terminar el programa.
"""

clientes = {100: {"nombre": "Juan", "direccion": "Santa Fe 100", "telefono": 100100, "correo": "juan@mail", "preferente": False},
            200: {"nombre": "Carlitos", "direccion": "Corrientes 200", "telefono": 200200, "correo": "carlitos@mail", "preferente": True}
}

def aniadir():
    nuevo_cliente = {}
    print("Ingrese los datos del nuevo cliente")
    cuit = int(input("CUIT: "))
    nombre = input("Nombre: ")
    nuevo_cliente["nombre"] = nombre
    direccion = input("Dirección: ")
    nuevo_cliente["direccion"] = direccion
    telefono = int(input("Teléfono: "))
    nuevo_cliente["telefono"] = telefono
    correo = input("Correo: ")
    nuevo_cliente["correo"] = correo
    preferente = False
    if input("Presione la tecla 'p' si es preferente") == 'p':
        preferente = True
    nuevo_cliente["preferente"] = preferente
    
    clientes[cuit] = nuevo_cliente # La clave es el CUIT, el valor es el diccionario con los datos del nuevo cliente


def eliminar():
    cuit = int(input("Ingrese CUIT del cliente a eliminar: "))
    if cuit in clientes:
        del clientes[cuit]
    else:
        print("El CUIT ingresado no existe")

def mostrar():
    cuit = int(input("Ingrese CUIT del cliente a mostrar: "))
    if cuit in clientes:
        print(clientes[cuit])
    else:
        print("El CUIT ingresado no existe")

def listar_todos():
    for clave in clientes.keys():
        cuit = clave
        nombre = clientes[clave]["nombre"]
        print(f"CUIT: {cuit} - Nombre: {nombre}")

def listar_preferentes():
    for clave in clientes.keys():
        if clientes[clave]["preferente"] == True:
            cuit = clave
            nombre = clientes[clave]["nombre"]
            print(f"CUIT: {cuit} - Nombre: {nombre}")

print("MENÚ")
print("1. Añadir cliente")
print("2. Eliminar cliente")
print("3. Mostrar cliente")
print("4. Listar todos los clientes")
print("5. Listar clientes preferentes")
print("6. Terminar")
opcion = input("Elija una opción: ")

while opcion != '6':
    if opcion == '1':
        aniadir()
    elif opcion == '2':
        eliminar()
    elif opcion == '3':
        mostrar()
    elif opcion == '4':
        listar_todos()
    elif opcion == '5':
        listar_preferentes()
    else:
        print("Opción no válida")
    opcion = input("Elija una opción: ")

#print(clientes)
print("Gracias, vuelva prontos")