from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton
from UI.interfaz_usuario import VentanaUsuario
from UI.interfaz_productos import VentanaProductos
from UI.interfaz_factura import VentanaFactura


class VentanaPrincipal(QMainWindow):
    def __init__(self, sistema_usuarios, sistema_stock, sistema_facturas):
        super().__init__()
        self.sistema_usuarios = sistema_usuarios
        self.sistema_stock = sistema_stock
        self.sistema_facturas = sistema_facturas
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Sistema de Facturación")
        self.setGeometry(100, 100, 800, 600)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        # Botones del menú principal
        btn_usuarios = QPushButton("Gestión de Usuarios")
        btn_usuarios.clicked.connect(self.mostrar_ventana_usuarios)

        btn_productos = QPushButton("Gestión de Productos")
        btn_productos.clicked.connect(self.mostrar_ventana_productos)

        btn_factura = QPushButton("Crear Factura")
        btn_factura.clicked.connect(self.mostrar_ventana_factura)

        # Agregar botones al layout
        layout.addWidget(btn_usuarios)
        layout.addWidget(btn_productos)
        layout.addWidget(btn_factura)

        central_widget.setLayout(layout)

        # Inicializar ventanas secundarias
        self.ventana_usuarios = None
        self.ventana_productos = None
        self.ventana_factura = None

    def mostrar_ventana_usuarios(self):
        if not self.ventana_usuarios:
            self.ventana_usuarios = VentanaUsuario(self.sistema_usuarios)
        self.ventana_usuarios.show()

    def mostrar_ventana_productos(self):
        if not self.ventana_productos:
            self.ventana_productos = VentanaProductos(self.sistema_stock)
        self.ventana_productos.show()

    def mostrar_ventana_factura(self):
        if not self.ventana_factura:
            self.ventana_factura = VentanaFactura(
                self.sistema_usuarios,
                self.sistema_stock,
                self.sistema_facturas
            )
        self.ventana_factura.show()