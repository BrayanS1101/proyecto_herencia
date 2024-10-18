from datetime import datetime


class Factura():
    def __init__(self,cliente):
        self.fecha = datetime.now()
        self.cliente = cliente
        self.productos = []
        self.valor_total = 0.0
    def producto_nuevo(self,producto):
        self.productos = self.productos.append(producto)
        self.valor_total += producto.precio_producto

