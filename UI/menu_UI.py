from crud.crear_factura import crear_factura 
from crud.crear_usuario import crear_usuario


class MenuUI:
    def __init__(self):
        self.cliente_crud = crear_usuario()
        self.factura_crud = crear_factura()

    def mostrar_menu(self):
        while True:
            print("1. Registrar cliente")
            print("2. Crear actura")
            print("3. Buscar cliente y sus facturas")
            print("4. Salir")
            
            opcion = input("\nIngrese una opcion: ")
            
            if opcion == "1":
                self.registrar_cliente()
            elif opcion == "2":
                self.crear_factura()
            elif opcion == "3":
                self.buscar_cliente()
            elif opcion == "4":
                print("Hasta pronto")
                break
            else:
                print("Intentelo de nuevo.")

    def registrar_cliente(self):
        cedula = input("Ingrese la cedula: ")
        if self.cliente_crud.buscar_por_cedula(cedula):
            print("Error: Cliente ya existe")
            return
        
        nombre = input("Ingrese nombre: ")
        apellido = input('Ingrese el apellido')

        cliente = self.cliente_crud.crear_cliente(cedula, nombre, apellido)
        if cliente:
            print(f"Registro hecho: {cliente}")
        else:
            print("Error")

    def crear_factura(self):
        cedula = input("Ingrese cedula del cliente: ")
        cliente = self.cliente_crud.buscar_por_cedula(cedula)
        
        if not cliente:
            print("No existe este este cliente")
            return
        
        try:
            monto = float(input("Ingrese el monto total de la factura: "))
            if monto <= 0:
                print("Error")
                return
        except ValueError:
            print("A ingresado un dato invalido")
            return
        '''	
            1.	try: En este bloque se coloca el código que podría causar una excepción. Python ejecuta este código y, si ocurre algún error, se detiene y salta al bloque except.
	        2.	except: Este bloque maneja el error especificado 
        '''

        factura = self.factura_crud.crear_factura(cliente, monto)
        print(factura)

    def buscar_cliente(self):
        cedula = input("Ingrese cedula: ")
        cliente = self.cliente_crud.buscar_por_cedula(cedula)
        
        if cliente:
            print(f"\nInformscion:\n{cliente}")
            
            facturas = self.factura_crud.buscar_facturas_cliente(cedula)
            if facturas:
                print("\nFacturas del cliente:")
                for factura in facturas:
                    print(factura)
            else:
                print("El cliente no tiene facturas registradas")
        else:
            print("Cliente no encontrado")
