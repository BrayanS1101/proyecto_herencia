from Modelo.fertilizantes import fertilizantes

def test_herencia():
    producto = fertilizantes("Insecticida ", 15.000, '8 dias', "ICA: 456", "15 de octubre")
    assert producto.frecuencia_aplicacion == '8 dias'
def test_atributos_propios():
    producto = fertilizantes("Insecticida ", 15.000, '8 dias', "ICA: 456", "15 de octubre")
    assert producto.fecha_ultima_aplicacion == '15 de octubre'