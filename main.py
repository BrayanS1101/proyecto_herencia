import sys
from PyQt5.QtWidgets import QApplication
from crud.crear_usuario import crear_usuario
from Modelo.stock import Stock
from crud.crear_factura import CrearFactura
from UI.ventana_principal import VentanaPrincipal

def main():
    # Inicializar la aplicación
    app = QApplication(sys.argv)

    # Inicializar los sistemas
    sistema_usuarios = crear_usuario()
    sistema_stock = Stock()
    sistema_facturas = CrearFactura(sistema_stock)

    # Crear y mostrar la ventana principal
    ventana_principal = VentanaPrincipal(
        sistema_usuarios,
        sistema_stock,
        sistema_facturas
    )
    ventana_principal.show()

    # Ejecutar la aplicación
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()