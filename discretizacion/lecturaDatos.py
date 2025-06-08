import pandas as pd
import numpy as np
import discretizacion.datosGenerales as gd  # Usamos gd para llamar variables globales


# Lectura de datos desde Excel
def leer_datos_desde_excel(ruta="datos/datos.xlsx"):
    #Creamos variables de nodos, datos y elementos.
    nodos = pd.read_excel(ruta, sheet_name="Nodos")
    datos = pd.read_excel(ruta, sheet_name="Datos")
    elementos = pd.read_excel(ruta, sheet_name="Elementos")
    props = pd.read_excel(ruta, sheet_name="Props")
    # Lectura de datos a variables globales
    gd.ndim = int(datos.values[0][0])
    gd.inf_nodos = nodos.values.tolist()
    gd.inf_elementos = elementos.values.tolist()

    #Inicializar EA propiedades
    gd.props= props.values.tolist()
    #definir numero de nodos
    gd.nn = len(nodos)
    #definir el numero de elementos
    gd.nels = len(elementos)
    #Inicializar la matriz nf (matriz con grados de libertad)
    gd.nf = np.zeros((gd.nn, gd.ndim))



