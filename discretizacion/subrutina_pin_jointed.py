import math

import numpy as np

import discretizacion.datosGenerales as gd

def pin_jointed():
    # define una lista de matriz vacia para elementos y para los km generados:
    elementos = []
    km_g = []
    # Iteración para recuperar valores de elementos y calcular las longitudes
    for fila in gd.inf_elementos:
        # Lectura de los valores de la segunda y tercera columna (valores de nodos)
        nodo_i = fila[1]
        nodo_j = fila[2]
        # Recuperacion y guardado de la información de nodos (x,y,z)
        coords_i = gd.inf_nodos[nodo_i][:3]  # Primeras 3 columnas del nodo_i
        coords_j = gd.inf_nodos[nodo_j][:3]  # Primeras 3 columnas del nodo_j

        # detalle para 1 dimension
        if gd.ndim == 1:
            ell = list(coords_i[0] - coords_j[0])
            gd.elementos.append(ell)
        # detalle para 2 dimensiones
        if gd.ndim == 2:
            # Toma de datos de las posiciones de nodos conectados
            x1 = coords_j[0]
            y1 = coords_j[1]
            x2 = coords_i[0]
            y2 = coords_i[1]
            # Cálculo de la longitud
            ell = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            # Cálculo de senos y cosenos
            cos = (x2 - x1) / ell
            sen = (y2 - y1) / ell
            # Cálculo de cosenos cuadrados, en variables para fácil lectura
            a = cos * cos
            b = sen * sen
            c = cos * sen
            # Recuperación del valor de EA
            ea_L = fila[0]
            # Cálculo y formación de la matriz km de 1 elemento:
            km_local = np.array([
                [a, c, -a, -c],
                [c, b, -c, -b],
                [-a, -c, a, c],
                [-c, -b, c, b]
            ])

            km_local = km_local * ea_L
            # Añadir el km local al km global
            km_g.append(km_local)
            # Añadir longitud a la fila de elementos
            completo = np.append(fila, ell)
            elementos.append(completo)
    # Ubicación de variables en memoria global:
    gd.elementos = np.array(elementos)
    gd.km_locales = km_g
