from Modelo.control_plagas import control_plagas
from Modelo.cliente import Cliente
from Modelo.fertilizantes import fertilizantes
from Modelo.factura import Factura
from Modelo.antibioticos import Antibioticos

def main():
    
    clienteX = Cliente("Brayan", "123456789")

    factura = Factura(clienteX)
    
    producto1 = control_plagas("SuperGrow", 10000, "cada 2 dias", "ICA :21213",'5 dias')
    producto2 = fertilizantes("BugAway", 80000,"cada 12 horas","REG-002", 'dos semanas')
    producto3 = Antibioticos("BoviCure", 150, 'bovino', "Bovino")

    factura.producto_nuevo(producto1)
    factura.producto_nuevo(producto2)
    factura.producto_nuevo(producto3)


    print(f"factura de {factura.cliente.nombre}") 
    print(f"precio total: {factura.valor_total}")  
if __name__ == "__main__":
    main()