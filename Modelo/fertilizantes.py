from .productos_control import productos_control

class fertilizantes(productos_control):
    def __init__(self, nombre_producto, precio_producto, frecuencia_aplicacion, registro_ICA,fecha_ultima_aplicacion):

        super().__init__(nombre_producto, precio_producto, frecuencia_aplicacion, registro_ICA)

        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion