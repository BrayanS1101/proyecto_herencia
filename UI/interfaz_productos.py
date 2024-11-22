from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                             QLineEdit, QPushButton, QMessageBox, QTableWidget,
                             QTableWidgetItem, QDoubleSpinBox, QSpinBox)


class VentanaProductos(QWidget):
    def __init__(self, sistema_stock):
        super().__init__()
        self.sistema_stock = sistema_stock
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Gestión de Productos")
        layout = QVBoxLayout()

        # Formulario de productos
        # Nombre
        nombre_layout = QHBoxLayout()
        nombre_label = QLabel("Nombre:")
        self.nombre_input = QLineEdit()
        nombre_layout.addWidget(nombre_label)
        nombre_layout.addWidget(self.nombre_input)

        # Cantidad
        cantidad_layout = QHBoxLayout()
        cantidad_label = QLabel("Cantidad:")
        self.cantidad_input = QSpinBox()
        self.cantidad_input.setRange(1, 9999)
        cantidad_layout.addWidget(cantidad_label)
        cantidad_layout.addWidget(self.cantidad_input)

        # Precio
        precio_layout = QHBoxLayout()
        precio_label = QLabel("Precio:")
        self.precio_input = QDoubleSpinBox()
        self.precio_input.setRange(0.01, 99999.99)
        self.precio_input.setPrefix("$")
        self.precio_input.setDecimals(2)
        precio_layout.addWidget(precio_label)
        precio_layout.addWidget(self.precio_input)

        # Botones
        botones_layout = QHBoxLayout()
        agregar_btn = QPushButton("Agregar Producto")
        agregar_btn.clicked.connect(self.agregar_producto)
        limpiar_btn = QPushButton("Limpiar")
        limpiar_btn.clicked.connect(self.limpiar_campos)

        botones_layout.addWidget(agregar_btn)
        botones_layout.addWidget(limpiar_btn)

        # Tabla de productos
        self.tabla_productos = QTableWidget()
        self.tabla_productos.setColumnCount(3)
        self.tabla_productos.setHorizontalHeaderLabels(["Nombre", "Cantidad", "Precio"])

        # Agregar layouts al principal
        layout.addLayout(nombre_layout)
        layout.addLayout(cantidad_layout)
        layout.addLayout(precio_layout)
        layout.addLayout(botones_layout)
        layout.addWidget(self.tabla_productos)

        self.setLayout(layout)
        self.actualizar_tabla()

    def agregar_producto(self):
        nombre = self.nombre_input.text()
        cantidad = self.cantidad_input.value()
        precio = self.precio_input.value()

        if not nombre:
            QMessageBox.warning(self, "Error", "El nombre del producto es requerido")
            return

        self.sistema_stock.agregar_producto(nombre, cantidad, precio)
        QMessageBox.information(self, "Éxito",
                                f"Producto agregado exitosamente:\n"
                                f"Nombre: {nombre}\n"
                                f"Cantidad: {cantidad}\n"
                                f"Precio: ${precio:.2f}")
        self.limpiar_campos()
        self.actualizar_tabla()

    def actualizar_tabla(self):
        self.tabla_productos.setRowCount(0)
        for nombre, datos in self.sistema_stock.productos.items():
            row = self.tabla_productos.rowCount()
            self.tabla_productos.insertRow(row)
            self.tabla_productos.setItem(row, 0, QTableWidgetItem(nombre))
            self.tabla_productos.setItem(row, 1,
                                         QTableWidgetItem(str(datos['cantidad'])))
            self.tabla_productos.setItem(row, 2,
                                         QTableWidgetItem(f"${datos['precio']:.2f}"))

    def limpiar_campos(self):
        self.nombre_input.clear()
        self.cantidad_input.setValue(1)
        self.precio_input.setValue(0.01)