import pandas as pd
import numpy as np

nodos = pd.read_excel("discretizacion/datos.xlsx",sheet_name="Nodos")
datos = pd.read_excel("discretizacion/datos.xlsx",sheet_name="Datos")
elementos = pd.read_excel("discretizacion/datos.xlsx",sheet_name="Elementos")

#Lectura de datos
ndim = datos.values[0][0]
inf_nodos=nodos.values.tolist()
inf_elementos=elementos.values.tolist()

#definicion de

nn=len(nodos)
neq=0

nels=len(elementos)

#nf matriz con libertad de nodos
#nn es el numero de nodos

nf=np.zeros((nn,ndim))

# inf_nodos[i][5] es la restriccion en X
# inf_nodos[i][6] es la restriccion en Y

for i in range(nn):
    for j in range(ndim):
        if inf_nodos[i][5 + j] == 1:
            # Si la columna 5+j es 1, ese DOF es libre → le asigno la próxima ecuación
            neq += 1
            nf[i][j] = neq
        else:
            # Si no es 1, lo dejo en 0 (DOF fijo)
            nf[i][j] = 0

print("El valor de nf es: ")
print(nf)

#Transformacion de inf_elementos de pandas a array
inf_elementos=np.array(inf_elementos)
#Las columnas 1,2 corresponden a las conectividades en i,j
num=inf_elementos[:,[1,2]]
print("El valor de num es: ")
print(num)
#Crear g en base a conectividad y nf
g=np.zeros((ndim*2,1))
g_g = np.zeros((nels, ndim * 2))

for i in range(nels):
    # Obtenemos los índices de los dos nodos de este elemento
    rest_x = (num[i, 0])
    rest_y = (num[i, 1])

    # Para cada dimensión, volcamos la restricción de rest_x en las columnas 0..ndim-1
    # y la de rest_y en las columnas ndim..(2*ndim - 1).
    for j in range(ndim):
        g_g[i, j] = nf[rest_x, j]          # grados de libertad de rest_x
        g_g[i, j + ndim] = nf[rest_y, j]   # grados de libertad de rest_y

# Al terminar:
print("Matriz g_g :")
print(g_g)









