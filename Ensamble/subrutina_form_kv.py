from numpy import zeros
from numpy.ma.core import not_equal

import discretizacion.datosGenerales as gd


def form_kv():
    print(gd.neq)
    kv = zeros(int(gd.neq + ((gd.neq - 1) * gd.neq / 2)))
    print(len(kv))
    for contador1 in range(len(gd.g_g)):
        g = gd.g_g[contador1, :]
        for i in range(2 * gd.ndim):
            if g[i] != 0:
                for j in range(2 * gd.ndim):
                    if g[j] != 0:
                        icd = g[j] - g[i] + 1
                        if (icd - 1) >= 0:
                            ival = int(gd.neq * (icd - 1) + g[i])
                            #print(ival)
                            kv[ival - 1] += gd.km_locales[contador1][i][j]
    if gd.ndim == 1 and kv[-1] == 0.0:
        kv = kv[:-1]
    gd.kv = kv
