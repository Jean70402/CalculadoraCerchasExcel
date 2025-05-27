
import discretizacion.lecturaDatos
import discretizacion.datosGenerales as gd
from discretizacion.subrutina_form_nf import subrutina_form_nf
from discretizacion.subrutina_num_to_g_g import subrutina_num_to_g_g
from discretizacion.subrutina_pin_jointed import pin_jointed

def main():
    #Lectura de datos de excel, y definir variables globales
    discretizacion.lecturaDatos.leer_datos_desde_excel()

    #Creación de matriz nf (gdl)
    subrutina_form_nf()

    #Creacion de matriz g_g (grados de libertad por elemento)
    subrutina_num_to_g_g()
    
    print("La matriz nf:")
    print(gd.nf)

    print("La matriz num:")
    print(gd.num)

    print("La matriz g_g:")
    print(gd.g_g)

    print("El ancho de banda es:")
    print(gd.nband)

    pin_jointed()

if __name__ == "__main__":
    main()
