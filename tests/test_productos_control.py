from Modelo.productos_control import productos_control

def test_herencia():
    producto =productos_control("Fertilizante", 20.000, "todos los dias", "ICA: 11")
    assert producto.nombre_producto == 'Fertilizante'
    assert producto.precio_producto == 20.000
def test_atributos_propios():
    producto =productos_control("Fertilizante", 20.000, "todos los dias", "ICA: 11")
    assert producto.frecuencia_aplicacion == 'todos los dias'
    assert producto.registro_ICA == 'ICA: 11'