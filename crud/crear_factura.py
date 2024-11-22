from Modelo.factura import Factura


class CrearFactura:
    def __init__(self, stock):
        self.facturas = []
        self.siguiente_numero = 1
        self.stock = stock

    def crear_factura(self, cliente, productos):
        factura = Factura(self.siguiente_numero, cliente,0.0)

        for nombre, (cantidad, precio) in productos.items():
            if self.stock.reducir_stock(nombre, cantidad):
                factura.producto_nuevo(nombre, cantidad, precio)
            else:
                print(f"Error al agregar {nombre}. Stock insuficiente o producto no disponible.")
                return None
        self.facturas.append(factura)
        cliente.agregar_factura_nueva(factura)
        self.siguiente_numero += 1

        print(f"Factura {factura.numero} creada  para {cliente.nombre} {cliente.apellido}.")
        return factura

    def buscar_facturas_cliente(self, cedula):
        facturas_cliente_buscado = []
        for factura in self.facturas:
            if factura.cliente.cedula == cedula:
                facturas_cliente_buscado.append(factura)
        return facturas_cliente_buscado


