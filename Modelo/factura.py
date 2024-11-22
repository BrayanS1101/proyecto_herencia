from datetime import datetime


class Factura():
    def __init__(self,numero_factura,cliente,monto):
        self.fecha = datetime.now()
        self.cliente = cliente
        self.productos = []
        self.valor_total = 0.0
        self.monto = monto
        self.numero_factura = numero_factura
    def producto_nuevo(self,producto,cantidad):
        total_producto = producto.precio_producto * cantidad
        self.productos.append((producto, cantidad))
        self.valor_total += total_producto

def __str__(self):
        return f"Factura {self.numero_factura} - Cliente: {self.cliente}, Monto: {self.monto}"



