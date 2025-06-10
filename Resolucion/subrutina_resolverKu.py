import numpy as np
import discretizacion.datosGenerales as gd


def subrutina_resolverKu():
    inv_mat = gd.inv_mat

    # Multiplicar
    result = inv_mat @ gd.loads_reducido
    gd.mat_def_u = result
    print(result)
