# Preguntar fecha de nacimiento y decir en qué estación nació (primavera, verano, otoño, invierno)

fecha = input("Ingrese fecha de nacimiento (dd-mm-aaaa): ")
dia = int(fecha[0:2]) # Recorto día y lo paso a entero
mes = int(fecha[3:5]) # Recorto mes y lo paso a entero

if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia < 21):
    print("Ud. nació en verano")
elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia > 21):
    print("Ud. nació en otoño")
elif (mes == 6 and dia >=21) or mes == 7 or mes == 8 or (mes == 9 and dia < 21):
    print("Ud. nació en invierno")
elif (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia < 21):
    print("Ud. nació en primavera")
else:
    print("Fecha inválida")