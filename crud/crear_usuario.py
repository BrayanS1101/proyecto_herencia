from Modelo.cliente import Cliente

class crear_usuario():
    def __init__(self):
        self.clientes_diccionario = {}

    def crear_cliente(self, cedula, nombre, apellido):
        if cedula not in self.clientes_diccionario:
            cliente = Cliente(nombre,apellido,cedula)
            self.clientes_diccionario[cedula] = cliente
            return cliente
        return None
    def buscar_por_cedula(self, cedula):
        return self.clientes_diccionario.get(cedula)

    
