import discretizacion.datosGenerales as gd


def insertarEa(prop):
    ea = gd.props[prop - 1][1]
    return ea *10


def insertarA(prop):
    a = gd.props[prop - 1][2]
    return a
