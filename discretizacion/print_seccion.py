
def print_seccion(titulo):
    ancho = 80
    print("\n" + "=" * ancho)
    print(titulo.center(ancho))
    print("=" * ancho + "\n")

import numpy as np

def print_nodos_formato(matriz, ndim):
    etiquetas = ['x', 'y', 'z'][:ndim]
    matriz = matriz.flatten()

    for i in range(0, len(matriz), ndim):
        linea = "      "
        for j in range(ndim):
            linea += f"         {etiquetas[j]}{(i//ndim)+1} = {matriz[i+j]:.2f}           "
        print(linea)
    print()

def print_elementos_formato_linea(matriz, nels):
    matriz = matriz.flatten()

    for i in range(nels):
        print(f"                          Barra {i + 1}   =   {matriz[i]:.2f}")

def print_seccion_titulo(titulo):
    ancho = 100
    decorador = "═"
    borde = f"{decorador * ancho}"
    titulo_centrado = f"╡ {titulo} ╞".center(ancho, " ")

    print("\n" + borde)
    print(titulo_centrado)
    print(borde + "\n")
