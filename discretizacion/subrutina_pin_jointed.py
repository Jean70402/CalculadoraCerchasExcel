
import discretizacion.datosGenerales as gd

import numpy as np
import math

def pin_jointed():

    elementos = []
    km_list = []

    for fila in gd.inf_elementos:
        nodo_i = fila[1]
        nodo_j = fila[2]

        coords_i = gd.inf_nodos[nodo_i ][:3]  # Primeras 3 columnas del nodo_i
        coords_j = gd.inf_nodos[nodo_j ][:3]  # Primeras 3 columnas del nodo_j

        #print(coords_i)
        #print(coords_j)

        if gd.ndim==1:
            ell=list(coords_i[0]-coords_j[0])
            gd.elementos.append(ell)

        if gd.ndim == 2:
            x1= coords_j[0]
            y1= coords_j[1]
            x2= coords_i[0]
            y2= coords_i[1]
            ell = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            cos=(x2-x1)/ell
            sen=(y2-y1)/ell
            a=cos*cos
            b=sen*sen
            c=cos*sen

            ea_L = fila[0]

            km_local = np.array([
                [ a,  c, -a, -c],
                [ c,  b, -c, -b],
                [-a, -c,  a,  c],
                [-c, -b,  c,  b]
            ])

            km_local=km_local*ea_L

            km_list.append(km_local)

            completo = np.append(fila, ell)  # Añadir longitud a la fila
            elementos.append(completo)

    gd.elementos = np.array(elementos)
    gd.km_locales = km_list
