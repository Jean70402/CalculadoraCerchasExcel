import numpy as np
import discretizacion.datosGenerales as gd

def form_global():
    total_dof = gd.nn * gd.ndim
    K = np.zeros((total_dof, total_dof))

    for idx in range(len(gd.km_locales)):
        # en lugar de inf_elementos, tomo la conexión de num
        ni, nj = gd.num[idx]              # ej: [2, 4]
        ni = int(ni)
        nj = int(nj)

        # armo la lista de DOFs físicos
        phys = (
                [ni * gd.ndim + d for d in range(gd.ndim)] +
                [nj * gd.ndim + d for d in range(gd.ndim)]
        )

        km = gd.km_locales[idx]           # 2*ndim × 2*ndim

        # ensamblado incondicional
        for a in range(2 * gd.ndim):
            for b in range(2 * gd.ndim):
                K[phys[a], phys[b]] += km[a][b]

    gd.kg = K
