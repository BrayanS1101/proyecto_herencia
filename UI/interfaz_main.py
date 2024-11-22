from crear_usuario import crear_usuario
from stock import Stock
from crear_factura import CrearFactura


def mostrar_menu():
    print("\n=== SISTEMA DE FACTURACIÓN ===")
    print("1. Crear Usuario")
    print("2. Agregar Producto")
    print("3. Buscar Cliente")
    print("4. Crear Factura")
    print("5. Salir")
    return input("Seleccione una opción: ")


def crear_nuevo_usuario(sistema_usuarios):
    print("\n=== CREAR NUEVO USUARIO ===")
    cedula = input("Ingrese la cédula: ")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")

    cliente = sistema_usuarios.crear_cliente(cedula, nombre, apellido)
    if cliente:
        print(f"\nCliente creado exitosamente: {cliente}")
    else:
        print("\nError: Ya existe un cliente con esa cédula")


def agregar_nuevo_producto(sistema_stock):
    print("\n=== AGREGAR NUEVO PRODUCTO ===")
    nombre = input("Ingrese el nombre del producto: ")

    try:
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio unitario: "))
        if cantidad <= 0 or precio <= 0:
            print("\nError: La cantidad y el precio deben ser mayores a 0")
            return

        sistema_stock.agregar_producto(nombre, cantidad, precio)
        print(f"\nProducto agregado exitosamente: {nombre} - Cantidad: {cantidad} - Precio: ${precio}")
    except ValueError:
        print("\nError: Por favor ingrese valores numéricos válidos")


def buscar_cliente(sistema_usuarios):
    print("\n=== BUSCAR CLIENTE ===")
    cedula = input("Ingrese la cédula del cliente: ")

    cliente = sistema_usuarios.buscar_por_cedula(cedula)
    if cliente:
        print(f"\nCliente encontrado: {cliente}")
        if cliente.facturas_cliente:
            print("\nFacturas del cliente:")
            for factura in cliente.facturas_cliente:
                print(f"Factura #{factura.numero_factura} - Fecha: {factura.fecha}")
    else:
        print("\nCliente no encontrado")


def crear_nueva_factura(sistema_usuarios, sistema_stock, sistema_facturas):
    print("\n=== CREAR NUEVA FACTURA ===")
    cedula = input("Ingrese la cédula del cliente: ")

    cliente = sistema_usuarios.buscar_por_cedula(cedula)
    if not cliente:
        print("\nError: Cliente no encontrado")
        return

    productos = {}
    while True:
        print("\nAgregar producto a la factura:")
        nombre = input("Nombre del producto (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break

        if nombre not in sistema_stock.productos:
            print("Error: Producto no encontrado en stock")
            continue

        try:
            cantidad = int(input("Cantidad: "))
            if cantidad <= 0:
                print("Error: La cantidad debe ser mayor a 0")
                continue

            precio = sistema_stock.obtener_precio(nombre)
            productos[nombre] = (cantidad, precio)
        except ValueError:
            print("Error: Por favor ingrese una cantidad válida")

    if productos:
        factura = sistema_facturas.crear_factura(cliente, productos)
        if factura:
            print(f"\nFactura creada exitosamente:")
            print(f"Cliente: {cliente}")
            print("Productos:")
            for nombre, (cantidad, precio) in productos.items():
                total = cantidad * precio
                print(f"- {nombre}: {cantidad} x ${precio} = ${total}")
            print(f"Total: ${factura.valor_total}")
    else:
        print("\nNo se agregaron productos a la factura")


def main():
    sistema_usuarios = crear_usuario()
    sistema_stock = Stock()
    sistema_facturas = CrearFactura(sistema_stock)

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            crear_nuevo_usuario(sistema_usuarios)
        elif opcion == "2":
            agregar_nuevo_producto(sistema_stock)
        elif opcion == "3":
            buscar_cliente(sistema_usuarios)
        elif opcion == "4":
            crear_nueva_factura(sistema_usuarios, sistema_stock, sistema_facturas)
        elif opcion == "5":
            print("\n¡Gracias por usar el sistema!")
            break
        else:
            print("\nOpción no válida. Por favor intente nuevamente.")


if __name__ == "__main__":
    main()