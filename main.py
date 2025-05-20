# main.py

import discretizacion.lecturaDatos
import discretizacion.datosGenerales as gd
from discretizacion.subrutina_form_nf import subrutina_form_nf
from discretizacion.subrutina_num_to_g_g import subrutina_num_to_g_g


def main():
    discretizacion.lecturaDatos.leer_datos_desde_excel()

    subrutina_form_nf()
    
    subrutina_num_to_g_g()
    
    print("La matriz nf:")
    print(gd.nf)

    print("La matriz num:")
    print(gd.num)

    print("La matriz g_g:")
    print(gd.g_g)

if __name__ == "__main__":
    main()
