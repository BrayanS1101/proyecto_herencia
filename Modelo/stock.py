class Stock:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, cantidad, precio):
        if nombre in self.productos:
            self.productos[nombre]['cantidad'] += cantidad
        else:
            self.productos[nombre] = {'cantidad': cantidad, 'precio': precio}

    def reducir_stock(self, nombre, cantidad):
        if nombre in self.productos and self.productos[nombre]['cantidad'] >= cantidad:
            self.productos[nombre]['cantidad'] -= cantidad
            return True
        else:
            return False

    def obtener_precio(self, nombre):
        if nombre in self.productos:
            return self.productos[nombre]['precio']
        return 0