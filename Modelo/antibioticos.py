from .producto import Producto

class Antibioticos(Producto):
    def __init__(self,nombre_producto,precio_producto,tipo_animal,dosis):

        super().__init__(nombre_producto,precio_producto)

        self.tipo_animal = tipo_animal
        self.dosis = dosis
    