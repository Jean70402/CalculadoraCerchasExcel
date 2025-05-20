
import pandas as pd
import numpy as np
import discretizacion.datosGenerales as gd  # Usamos gd
from discretizacion.subrutina_form_nf import subrutina_form_nf
from discretizacion.subrutina_num_to_g_g import subrutina_num_to_g_g


# Lectura de datos desde Excel
def leer_datos_desde_excel(ruta="datos/datos.xlsx"):
    nodos = pd.read_excel(ruta, sheet_name="Nodos")
    datos = pd.read_excel(ruta, sheet_name="Datos")
    elementos = pd.read_excel(ruta, sheet_name="Elementos")

    # Lectura de datos
    gd.ndim = int(datos.values[0][0])
    gd.inf_nodos = nodos.values.tolist()
    gd.inf_elementos = elementos.values.tolist()

    #definir numero de nodos
    gd.nn = len(nodos)
    #definir el numero de elementos
    gd.nels = len(elementos)
    #Inicializar la matriz nf (matriz con grados de libertad)
    gd.nf = np.zeros((gd.nn, gd.ndim))
