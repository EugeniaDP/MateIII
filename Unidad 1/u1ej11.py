"""
* Generar una matriz "mat" de 4x4 con datos random
* Obtener la suma de los valores de mat
* Obtener la desviación estándar de los valores de mat
* Obtener las sumas de las columnas de mat
"""

import numpy as np

mat = np.random.random((4, 4))
print(mat)
print("Suma de todos los elementos:", np.sum(mat))
print("Desviación estándar de los elementos:", np.std(mat))
print("Suma de los elementos de las columnas:", np.sum(mat, axis=0))