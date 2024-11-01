from .producto import Producto

class productos_control(Producto):
    def __init__(self,nombre_producto,precio_producto,frecuencia_aplicacion,registro_ICA):

        super().__init__(nombre_producto,precio_producto)

        self.frecuencia_aplicacion = frecuencia_aplicacion
        self.registro_ICA = registro_ICA