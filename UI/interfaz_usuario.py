from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                             QLineEdit, QPushButton, QMessageBox, QTableWidget,
                             QTableWidgetItem)
from PyQt5.QtCore import Qt


class VentanaUsuario(QWidget):
    def __init__(self, sistema_usuarios):
        super().__init__()
        self.sistema_usuarios = sistema_usuarios
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Gestión de Usuarios")
        layout = QVBoxLayout()

        # Formulario de creación
        form_layout = QVBoxLayout()

        # Cédula
        cedula_layout = QHBoxLayout()
        cedula_label = QLabel("Cédula:")
        self.cedula_input = QLineEdit()
        cedula_layout.addWidget(cedula_label)
        cedula_layout.addWidget(self.cedula_input)

        # Nombre
        nombre_layout = QHBoxLayout()
        nombre_label = QLabel("Nombre:")
        self.nombre_input = QLineEdit()
        nombre_layout.addWidget(nombre_label)
        nombre_layout.addWidget(self.nombre_input)

        # Apellido
        apellido_layout = QHBoxLayout()
        apellido_label = QLabel("Apellido:")
        self.apellido_input = QLineEdit()
        apellido_layout.addWidget(apellido_label)
        apellido_layout.addWidget(self.apellido_input)

        # Botones
        botones_layout = QHBoxLayout()
        crear_btn = QPushButton("Crear Usuario")
        crear_btn.clicked.connect(self.crear_usuario)
        buscar_btn = QPushButton("Buscar Usuario")
        buscar_btn.clicked.connect(self.buscar_usuario)
        limpiar_btn = QPushButton("Limpiar")
        limpiar_btn.clicked.connect(self.limpiar_campos)

        botones_layout.addWidget(crear_btn)
        botones_layout.addWidget(buscar_btn)
        botones_layout.addWidget(limpiar_btn)

        # Tabla de facturas
        self.tabla_facturas = QTableWidget()
        self.tabla_facturas.setColumnCount(3)
        self.tabla_facturas.setHorizontalHeaderLabels(["Número", "Fecha", "Valor Total"])
        self.tabla_facturas.hide()

        # Agregar todos los layouts al layout principal
        layout.addLayout(cedula_layout)
        layout.addLayout(nombre_layout)
        layout.addLayout(apellido_layout)
        layout.addLayout(botones_layout)
        layout.addWidget(self.tabla_facturas)

        self.setLayout(layout)

    def crear_usuario(self):
        cedula = self.cedula_input.text()
        nombre = self.nombre_input.text()
        apellido = self.apellido_input.text()

        if not all([cedula, nombre, apellido]):
            QMessageBox.warning(self, "Error", "Todos los campos son requeridos")
            return

        cliente = self.sistema_usuarios.crear_cliente(cedula, nombre, apellido)
        if cliente:
            QMessageBox.information(self, "Éxito",
                                    f"Cliente creado exitosamente:\n{cliente}")
            self.limpiar_campos()
        else:
            QMessageBox.warning(self, "Error",
                                "Ya existe un cliente con esa cédula")

    def buscar_usuario(self):
        cedula = self.cedula_input.text()
        if not cedula:
            QMessageBox.warning(self, "Error", "Ingrese una cédula para buscar")
            return

        cliente = self.sistema_usuarios.buscar_por_cedula(cedula)
        if cliente:
            self.nombre_input.setText(cliente.nombre)
            self.apellido_input.setText(cliente.apellido)
            self.mostrar_facturas(cliente)
            QMessageBox.information(self, "Cliente Encontrado",
                                    f"Cliente encontrado: {cliente}")
        else:
            QMessageBox.warning(self, "Error", "Cliente no encontrado")
            self.tabla_facturas.hide()

    def mostrar_facturas(self, cliente):
        self.tabla_facturas.setRowCount(0)
        if cliente.facturas_cliente:
            self.tabla_facturas.show()
            for factura in cliente.facturas_cliente:
                row = self.tabla_facturas.rowCount()
                self.tabla_facturas.insertRow(row)
                self.tabla_facturas.setItem(row, 0,
                                            QTableWidgetItem(str(factura.numero)))
                self.tabla_facturas.setItem(row, 1,
                                            QTableWidgetItem(factura.fecha.strftime("%Y-%m-%d %H:%M")))
                self.tabla_facturas.setItem(row, 2,
                                            QTableWidgetItem(f"${factura.valor_total:.2f}"))
        else:
            self.tabla_facturas.hide()

    def limpiar_campos(self):
        self.cedula_input.clear()
        self.nombre_input.clear()
        self.apellido_input.clear()
        self.tabla_facturas.hide()