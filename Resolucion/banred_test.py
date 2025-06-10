import numpy as np

# Matriz simétrica definida positiva con 2 bandas
A = np.array([
    [4, 1, 0, 0, 0, 0],
    [1, 5, 2, 0, 3, 0],
    [0, 2, 6, 1, 0, 0],
    [0, 0, 1, 7, 2, 0],
    [0, 3, 0, 2, 8, 1],
    [0, 0, 0, 0, 1, 9]
], dtype=float)

n = A.shape[0]
print(n)
bw = 3  # número de bandas

def to_band_matrix(A, bw):
    n = A.shape[0]
    band = np.zeros((bw+1, n))
    for i in range(n):
        for j in range(bw+1):
            if i + j < n:
                band[j, i] = A[i, i+j]
    return band

def print_band(band):
    print("Matriz en formato banda:")
    for i in range(band.shape[0]):
        print(f"Banda {i}: {band[i]}")

# Factorización Cholesky para matriz banda simétrica definida positiva
def cholesky_band(band, bw):
    n = band.shape[1]
    print(n)
    L = np.zeros_like(band)
    print(L)
    for j in range(n):
        sum_diag = 0.0
        for k in range(1, bw+1):
            if j - k < 0:
                break
            sum_diag += L[k, j - k]**2
        L[0, j] = np.sqrt(band[0, j] - sum_diag)

        for i in range(1, bw+1):
            if j + i >= n:
                break
            sum_off = 0.0
            for k in range(1, bw - i + 1):
                if j - k < 0 or j + i - k < 0:
                    break
                sum_off += L[k, j - k] * L[k + i, j - k]
            L[i, j] = (band[i, j] - sum_off) / L[0, j]

    return L

# Resolver L y = b (L es banda inferior con diagonales en L[0, :])
def forward_substitution_band(L, bw, b):
    n = len(b)
    y = np.zeros_like(b)

    for i in range(n):
        s = b[i]
        for k in range(1, min(bw+1, i+1)):
            s -= L[k, i - k] * y[i - k]
        y[i] = s / L[0, i]
    return y

# Resolver L.T x = y (L.T es banda superior)
def backward_substitution_band(L, bw, y):
    n = len(y)
    x = np.zeros_like(y)

    for i in reversed(range(n)):
        s = y[i]
        for k in range(1, min(bw+1, n - i)):
            s -= L[k, i] * x[i + k]
        x[i] = s / L[0, i]
    return x

# Construir matriz banda
bandA = to_band_matrix(A, bw)
print_band(bandA)

# Factorizar
L = cholesky_band(bandA, bw)
print("\nFactorización Cholesky (matriz banda L):")
print_band(L)

# Invertir A resolviendo Ax = e_j para j=0..n-1
invA = np.zeros((n, n))
for j in range(n):
    e = np.zeros(n)
    e[j] = 1.0
    y = forward_substitution_band(L, bw, e)
    x = backward_substitution_band(L, bw, y)
    invA[:, j] = x

print("\nInversa calculada con factorización Cholesky en formato banda:")
print(invA)

invA_direct = np.linalg.inv(A)
print("\nInversa calculada con numpy.linalg.inv:")
print(invA_direct)

diff = np.abs(invA - invA_direct)
print("\nDiferencia absoluta entre ambas inversas:")
print(diff)
print(f"\nMáxima diferencia: {np.max(diff)}")
