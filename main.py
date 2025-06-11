import discretizacion.datosGenerales as gd
import discretizacion.lecturaDatos
from Ensamble.subrutina_form_kv import form_kv
from Ensamble.subrutina_loads import calcular_loads
from Ensamble.subrutina_pin_jointed import pin_jointed
from Postprocesamiento.subrutina_postprocesamiento import obtener_mat_def_completa, transformar_barra_angulo, \
    obtenerReacciones
from Resolucion.subrutina_banred import subrutina_banred
from Resolucion.subrutina_resolverKu import subrutina_resolverKu
from discretizacion.subrutina_form_nf import subrutina_form_nf
from discretizacion.subrutina_num_to_g_g import subrutina_num_to_g_g
from discretizacion.print_seccion import print_seccion, print_seccion_titulo


def main():
    print_seccion_titulo("Calculadora de Cerchas 1d,2d,3d")
    # Lectura de datos de excel, y definir variables globales
    discretizacion.lecturaDatos.leer_datos_desde_excel()

    # Creación de matriz nf (gdl)
    subrutina_form_nf()

    # Creacion de matriz g_g (grados de libertad por elemento)
    subrutina_num_to_g_g()

    # Creación de elementos de matriz de rigidez locales y
    # transformación a globales para ensamble, guardados en km
    pin_jointed()

    # Ensamble del vector kv, que toma la diagonal principal
    # y la sección triangular superior para aprovechar simetría
    form_kv()

    # Recupera el vector de fuerzas, cálculo del vector reducido
    calcular_loads()

    print_seccion("La matriz nf:")
    print(gd.nf)

    print_seccion("La matriz num:")
    print(gd.num)

    print_seccion("La matriz g_g:")
    print(gd.g_g)

    print_seccion("El ancho de banda es:")
    print(gd.nband)

    print_seccion("Primer km local:")
    print(gd.km_locales[0])

    print_seccion("El vector de kv:")
    print(gd.kv)

    print_seccion("La matriz de fuerzas (kN): ")
    print(gd.loads)

    print_seccion("Reducción mediante cholesky y sustitución mediante Gauss modificado (kv):")
    subrutina_banred()

    # Resolucion de F=k*u, para obtener deformaciones

    subrutina_resolverKu()

    #Subrutinas de postprocesamiento, incluyendo calcular nuevamente
    # la matriz de rigidez global y de deformaciones completas
    print_seccion_titulo("Postprocesamiento")
    obtener_mat_def_completa()
    transformar_barra_angulo()
    obtenerReacciones()

if __name__ == "__main__":
    main()
