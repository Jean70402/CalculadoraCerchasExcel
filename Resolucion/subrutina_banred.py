import numpy as np

import discretizacion.datosGenerales as gd
from Resolucion.subrutina_backsub import backward_substitution_band,forward_substitution_band

def subrutina_banred():
    print("Aqui viene Banred")
    n = gd.neq
    print(n)
    bk = np.array(gd.kv)
    bk_ordenado = bk.reshape(-1, n)
    bw = int(gd.nband)
    L = cholesky_band(bk_ordenado, bw)
    inv_mat = np.zeros((n, n))
    for j in range(n):
        e = np.zeros(n)
        e[j] = 1.0
        y = forward_substitution_band(L, bw, e)
        x = backward_substitution_band(L, bw, y)
        inv_mat[:, j] = x
    print("Inversa de la matriz reducida es:")
    gd.inv_mat = inv_mat
    print(inv_mat)

def cholesky_band(band, bw):
    n = band.shape[1]
    L = np.zeros_like(band)
    for j in range(n):
        sum_diag = 0.0
        for k in range(1, bw + 1):
            if j - k < 0 or k >= band.shape[0]:
                break
            sum_diag += L[k, j - k] ** 2
        L[0, j] = np.sqrt(band[0, j] - sum_diag)

        for i in range(1, bw + 1):
            if j + i >= n or i >= band.shape[0]:
                break
            sum_off = 0.0
            for k in range(1, bw - i + 1):
                if j - k < 0 or j + i - k < 0 or (k + i) >= band.shape[0] or k >= band.shape[0]:
                    break
                sum_off += L[k, j - k] * L[k + i, j - k]
            L[i, j] = (band[i, j] - sum_off) / L[0, j]
    return L

