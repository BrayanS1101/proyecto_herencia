from Modelo.factura import Factura
from Modelo.cliente import Cliente
from Modelo.control_plagas import control_plagas


def test_creacion_factura():
    cliente = Cliente("Brayan", "ortiz",10893434)
    factura = Factura(cliente)
    producto = control_plagas("Insecticida ", 15.000, '8 dias', "ICA: 456", "5 dias")
    factura.producto_nuevo(producto)

    assert factura.cliente.nombre== 'Brayan'
    

