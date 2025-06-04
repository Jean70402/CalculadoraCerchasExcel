from numpy import zeros
from numpy.ma.core import not_equal

import discretizacion.datosGenerales as gd


def form_kv():
    kv = zeros(int(gd.neq * (gd.neq + 1) / 2))
    for contador1 in range(len(gd.g_g)):
        g = gd.g_g[contador1, :]
        for i in range(2 * gd.ndim):
            if g[i] != 0:
                for j in range(2 * gd.ndim):
                    if g[j] != 0:
                        icd = g[j] - g[i] + 1
                        ival = int(gd.neq * (icd - 1) + g[i])
                        kv[ival - 1] += gd.km_locales[contador1][i][j]
    gd.kv = kv

