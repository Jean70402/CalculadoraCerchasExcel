import discretizacion.datosGenerales as gd  # Usamos gd


def subrutina_form_nf():
    # iteracion para definir el nf(matriz de grados de libertad, enumerados los libres)
    for i in range(gd.nn):
        for j in range(gd.ndim):
            # Si encuentra un 1 en la iteracion, suma en 1 neq y reemplaza en nf
            if gd.inf_nodos[i][5 + j] == 1:
                gd.neq += 1
                gd.nf[i][j] = gd.neq
            else:
                # Si no, pasa al siguiente valor y lo deja como 0 (como mis notas)
                gd.nf[i][j] = 0
