from Modelo.control_plagas import control_plagas

def test_herencia():
    producto = control_plagas("Insecticida ", 15.000, '8 dias', "ICA: 456", "5 dias")
    assert producto.registro_ICA == 'ICA: 456'
def test_atributos_propios():
    producto = control_plagas("Insecticida ", 15.000, '8 dias', "ICA: 456", "5 dias")
    assert producto.periodo_carencia == '5 dias'