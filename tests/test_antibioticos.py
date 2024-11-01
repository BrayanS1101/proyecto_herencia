from Modelo.antibioticos import Antibioticos

def test_herencia():
    medicamento = Antibioticos("Penicilina", 10.000, "Bovino", "500mg")
    assert medicamento.nombre_producto =="Penicilina"
def test_atributos_propios():
    medicamento = Antibioticos("Penicilina", 10.000, "Bovino", "500mg")
    assert medicamento.dosis == '500mg'

