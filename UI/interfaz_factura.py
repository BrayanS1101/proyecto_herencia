from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                             QLineEdit, QPushButton, QMessageBox, QTableWidget,
                             QTableWidgetItem, QSpinBox, QComboBox)


class VentanaFactura(QWidget):
    def __init__(self, sistema_usuarios, sistema_stock, sistema_facturas):
        super().__init__()
        self.sistema_usuarios = sistema_usuarios
        self.sistema_stock = sistema_stock
        self.sistema_facturas = sistema_facturas
        self.productos_seleccionados = {}
        self.cliente_actual = None
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Crear Factura")
        layout = QVBoxLayout()

        # Sección cliente
        cliente_layout = QHBoxLayout()
        cedula_label = QLabel("Cédula del cliente:")
        self.cedula_input = QLineEdit()
        buscar_btn = QPushButton("Buscar")
        buscar_btn.clicked.connect(self.buscar_cliente)
        cliente_layout.addWidget(cedula_label)
        cliente_layout.addWidget(self.cedula_input)
        cliente_layout.addWidget(buscar_btn)

        # Info del cliente
        self.info_cliente = QLabel("")

        # Sección productos
        productos_layout = QHBoxLayout()
        self.producto_combo = QComboBox()
        self.actualizar_combo_productos()
        self.cantidad_spin = QSpinBox()
        self.cantidad_spin.setRange(1, 9999)
        agregar_producto_btn = QPushButton("Agregar a la factura")
        agregar_producto_btn.clicked.connect(self.agregar_producto_factura)

        productos_layout.addWidget(QLabel("Producto:"))
        productos_layout.addWidget(self.producto_combo)
        productos_layout.addWidget(QLabel("Cantidad:"))
        productos_layout.addWidget(self.cantidad_spin)
        productos_layout.addWidget(agregar_producto_btn)

        # Tabla de productos en la factura
        self.tabla_productos = QTableWidget()
        self.tabla_productos.setColumnCount(4)
        self.tabla_productos.setHorizontalHeaderLabels(
            ["Producto", "Cantidad", "Precio Unit.", "Total"])

        # Botones finales
        botones_layout = QHBoxLayout()
        crear_factura_btn = QPushButton("Crear Factura")
        crear_factura_btn.clicked.connect(self.crear_factura)
        cancelar_btn = QPushButton("Cancelar")
        cancelar_btn.clicked.connect(self.limpiar_todo)

        botones_layout.addWidget(crear_factura_btn)
        botones_layout.addWidget(cancelar_btn)

        # Total
        self.total_label = QLabel("Total: $0.00")


        layout.addLayout(cliente_layout)
        layout.addWidget(self.info_cliente)
        layout.addLayout(productos_layout)
        layout.addWidget(self.tabla_productos)
        layout.addWidget(self.total_label)
        layout.addLayout(botones_layout)

        self.setLayout(layout)

    def actualizar_combo_productos(self):
        self.producto_combo.clear()
        for nombre in self.sistema_stock.productos.keys():
            self.producto_combo.addItem(nombre)

    def buscar_cliente(self):
        cedula = self.cedula_input.text()
        if not cedula:
            QMessageBox.warning(self, "Error", "Ingrese una cédula")
            return

        self.cliente_actual = self.sistema_usuarios.buscar_por_cedula(cedula)
        if self.cliente_actual:
            self.info_cliente.setText(
                f"Cliente: {self.cliente_actual.nombre} {self.cliente_actual.apellido}")
        else:
            QMessageBox.warning(self, "Error", "Cliente no encontrado")
            self.info_cliente.setText("")
            self.cliente_actual = None

    def agregar_producto_factura(self):
        if not self.cliente_actual:
            QMessageBox.warning(self, "Error", "Primero seleccione un cliente")
            return

        producto = self.producto_combo.currentText()
        if not producto:  # Si no hay productos en el combo
            QMessageBox.warning(self, "Error", "No hay productos disponibles")
            return

        cantidad = self.cantidad_spin.value()

        if producto not in self.sistema_stock.productos:
            QMessageBox.warning(self, "Error", "Producto no disponible")
            return

        stock_disponible = self.sistema_stock.productos[producto]['cantidad']
        if cantidad > stock_disponible:
            QMessageBox.warning(self, "Error", f"Stock insuficiente. Disponible: {stock_disponible}")
            return

        precio = self.sistema_stock.productos[producto]['precio']
        self.productos_seleccionados[producto] = (cantidad, precio)
        self.actualizar_tabla_productos()

    def actualizar_tabla_productos(self):
        self.tabla_productos.setRowCount(0)
        total = 0

        for nombre, (cantidad, precio) in self.productos_seleccionados.items():
            row = self.tabla_productos.rowCount()
            self.tabla_productos.insertRow(row)
            subtotal = cantidad * precio
            total += subtotal

            self.tabla_productos.setItem(row, 0, QTableWidgetItem(nombre))
            self.tabla_productos.setItem(row, 1, QTableWidgetItem(str(cantidad)))
            self.tabla_productos.setItem(row, 2, QTableWidgetItem(f"${precio:.2f}"))
            self.tabla_productos.setItem(row, 3, QTableWidgetItem(f"${subtotal:.2f}"))

        self.total_label.setText(f"Total: ${total:.2f}")

    def crear_factura(self):
        if not self.cliente_actual:
            QMessageBox.warning(self, "Error", "Seleccione un cliente")
            return

        if not self.productos_seleccionados:
            QMessageBox.warning(self, "Error", "Agregue productos a la factura")
            return

        try:
            factura = self.sistema_facturas.crear_factura(
                self.cliente_actual,
                self.productos_seleccionados
            )

            if factura:
                QMessageBox.information(
                    self,
                    "Éxito",
                    f"Factura #{factura.numero} creada exitosamente\n"
                    f"Total: ${factura.valor_total:.2f}"
                )
                self.limpiar_todo()
            else:
                QMessageBox.warning(self, "Error", "Error al crear la factura")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al crear la factura: {str(e)}")

    def limpiar_todo(self):
        self.cedula_input.clear()
        self.info_cliente.setText("")
        self.cantidad_spin.setValue(1)
        self.productos_seleccionados.clear()
        self.cliente_actual = None
        self.actualizar_tabla_productos()