from .productos_control import productos_control

class control_plagas(productos_control):
    def __init__(self, nombre_producto, precio_producto, frecuencia_aplicacion, registro_ICA,periodo_carencia):

        super().__init__(nombre_producto, precio_producto, frecuencia_aplicacion, registro_ICA)

        self.periodo_carencia = periodo_carencia
        