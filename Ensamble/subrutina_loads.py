import numpy as np

import discretizacion.datosGenerales as gd

def calcular_loads():
    dim = gd.ndim  # 1, 2 o 3
    loads = [nodo[3:3+dim] for nodo in gd.inf_nodos]

    gdl_libres = []
    gdl_completos=[]
    for i in range(gd.nn):
        for j in range(dim):
            if gd.inf_nodos[i][6 + j] == 1:
                gdl_libres.append(i * dim + j)  # índice global de GDL libre
                gdl_completos.append(i * dim + j)
            else:
                gdl_completos.append(0)
    loads_array = np.array(loads)
    loads_col = loads_array.flatten()[:, np.newaxis]  # Vector columna completo
    gd.loads = loads_col
    # print("GDL libres:"+str(gdl_libres))
    gd.gdl_completos = gdl_completos
    # Reducción: selecciona solo los GDL libres
    loads_reducido = loads_col[gdl_libres]
    gd.loads_reducido=loads_reducido
    #print("Cargas reducidas:")
    #print(gd.loads_reducido)
