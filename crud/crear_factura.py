from Modelo.factura import Factura
from Modelo.cliente import Cliente

class crear_factura:
    def __init__(self):
        self.facturas = []
        self.siguiente_numero = 1

    def crear_factura(self, cliente,monto):
        factura = Factura(self.siguiente_numero, cliente,monto)
        self.facturas.append(factura)
        cliente.agregar_factura_nueva(factura)
        self.siguiente_numero += 1
        return factura

    def buscar_facturas_cliente(self, cedula):
        facturas_cliente_buscado= []
        for factura_buscar in self.facturas:
                if factura_buscar.cliente.cedula == cedula:
                    facturas_cliente_buscado.append(factura_buscar)
        return facturas_cliente_buscado
