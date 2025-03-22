# Contar cuántas veces aparece la letra "a" en el string "letras"

letras = "aofnmgfoiajgmipoafjgmvaporgjmaeporgvmeñfvjkaeñvknmarvnampvma{rvkameñr vkmaevlkaekvamlvnalvkaerjvakpvna{eñrvnaerv"
contador = 0
for letra in letras:
    if letra == "a":
        contador += 1
print(f"La letra 'a' aparece {contador} veces en el string 'letras'")