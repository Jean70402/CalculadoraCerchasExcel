import discretizacion.datosGenerales as gd


def calcular_loads():
    dim = gd.ndim  # 1, 2 o 3
    loads = [nodo[3:3+dim] for nodo in gd.inf_nodos]
    gd.loads = loads