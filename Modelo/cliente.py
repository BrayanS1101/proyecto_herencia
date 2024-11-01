class Cliente:
    def __init__(self,nombre,apellido,cedula):

        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.facturas_cliente = []

    def agregar_factura_nueva(self,factura):
        self.facturas_cliente.append(factura)
    def __str__(self):
        return f"{self.nombre} {self.apellido} (cedula: {self.cedula})"