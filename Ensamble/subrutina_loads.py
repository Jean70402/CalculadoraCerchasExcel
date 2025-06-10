import numpy as np

import discretizacion.datosGenerales as gd

def calcular_loads():
    dim = gd.ndim  # 1, 2 o 3
    loads = [nodo[3:3+dim] for nodo in gd.inf_nodos]
    gd.loads=loads
    gdl_libres = []

    for i in range(gd.nn):
        for j in range(dim):
            if gd.inf_nodos[i][6 + j] == 1:
                gdl_libres.append(i * dim + j)  # índice global de GDL libre

    loads_array = np.array(loads)
    loads_col = loads_array.flatten()[:, np.newaxis]  # Vector columna completo

    # Reducción: selecciona solo los GDL libres
    loads_reducido = loads_col[gdl_libres]
    gd.loads_reducido=loads_reducido
    print("Cargas reducidas:")
    print(gd.loads_reducido)
