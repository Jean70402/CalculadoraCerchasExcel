import discretizacion.lecturaDatos
import discretizacion.datosGenerales as gd
from Ensamble.subrutina_form_kv import form_kv
from discretizacion.subrutina_form_nf import subrutina_form_nf
from discretizacion.subrutina_num_to_g_g import subrutina_num_to_g_g
from Ensamble.subrutina_pin_jointed import pin_jointed


def main():
    # Lectura de datos de excel, y definir variables globales
    discretizacion.lecturaDatos.leer_datos_desde_excel()

    # Creación de matriz nf (gdl)
    subrutina_form_nf()

    # Creacion de matriz g_g (grados de libertad por elemento)
    subrutina_num_to_g_g()

    #Creación de elementos de matriz de rigidez locales y
    #transformación a globales para ensamble, guardados en km
    pin_jointed()

    #Ensamble del vector kv, que toma la diagonal principal
    #y la sección triangular superior para aprovechar simetría
    form_kv()

    print("La matriz nf:")
    
    print("La matriz nf:")
    print(gd.nf)

    print("La matriz num:")
    print(gd.num)

    print("La matriz g_g:")
    print(gd.g_g)

    print("El ancho de banda es:")
    print(gd.nband)

    print("Primer km local:")
    print(gd.km_locales[1])

    print("El vector de kv:")
    print(gd.kv)

if __name__ == "__main__":
    main()
