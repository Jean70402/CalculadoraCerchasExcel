import discretizacion.datosGenerales as gd


def insertarEa(prop):
    ea = gd.props[prop - 1][1]
    return ea
    #ADVERTENCIA: "MODIFICAR ESTO DAÑA TODO EL PROGRAMA "
    #return ea*100


def insertarA(prop):
    a = gd.props[prop - 1][2]
    return a
