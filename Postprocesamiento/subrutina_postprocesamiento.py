import math

import numpy as np

import discretizacion.datosGenerales as gd  # Usamos gd
from discretizacion.insertarEA import insertarEa
from Ensamble.subrutina_form_global import form_global

def obtener_mat_def_completa():
    u = gd.mat_def_u  # vector columna con las deformaciones activas
    u_completa = []

    # Contador para recorrer el vector u (solo los gdl activos)
    contador_u = 0

    for gdl in gd.gdl_completos:
        if gdl == 0:
            u_completa.append(0.0)
        else:
            u_completa.append(u[contador_u, 0])
            contador_u += 1

    # Convertimos a array columna
    print("Vector u_completo:")
    gd.u_completa = np.array(u_completa).reshape(-1, 1)
    print(gd.u_completa)


def transformar_barra_angulo():
    # define una lista de matriz vacia para elementos y para los km generados:
    axiales = []
    # Iteración para recuperar valores de elementos y calcular las longitudes
    for idx, fila in enumerate(gd.inf_elementos):
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

            mat_angulo = np.array([
                [cos, sen, 0, 0],
                [0, 0, cos, sen]
            ])
            #print(mat_angulo)
            conex = gd.g_g[idx]  # por ejemplo: array([0., 0., 3., 4.])
            conex = conex.astype(int)  # aseguramos enteros para índices

            u_global = np.zeros((2 * gd.ndim, 1))  # inicializa vector columna con ceros

            for i in range(2 * gd.ndim):
                if conex[i] != 0:
                    u_global[i, 0] = gd.u_completa[conex[i] + 1, 0]  # asigna valor desde u_completa
            #print(u_global)
            u_local = mat_angulo @ u_global
            #print(u_local)
            ea = insertarEa(fila[0])
            ea_L = ea / ell
            axial = ea_L * (u_local[0] - u_local[1])
            if abs(axial) < 1e-8:
                axial = 0.0
                axiales.append(axial)
            else:
                axiales.append(axial.item())

    axiales = np.array(axiales)[:, np.newaxis]
    print("Los axiales son: ")
    print(axiales)

def obtenerReacciones():
    form_global()

    # Calculo de las reacciones
    reacciones = (gd.kg @ gd.u_completa) - gd.loads

    # Redondear a 2 decimales y eliminar residuos numéricos cercanos a cero
    reacciones = np.where(np.abs(reacciones) < 1e-12, 0, np.round(reacciones, 2))
    print("Las reacciones son:")
    print(reacciones)
    return reacciones

