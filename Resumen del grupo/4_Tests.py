
#! VER DESPUES DE POO_herencia

'''
Tests: Es una forma de comprobar que un conjunto de funciones o clases (tantas como queramos) funcionan como esperamos. 
    Lógicamente, las pruebas unitarias nunca pueden garantizar completamente el correcto funcionamiento de una porción de código. 
    No obstante ello, serán capaces de detectar gran cantidad de anomalías y de ahorrarnos tiempo de depuración.

    - Se importa mediante: 

        import unittest

    - Se ejecuta mediante:

        if __name__ == '__main__':
            unittest.main()
    
      Al final del codigo
'''

'''
Aclaraciones importantes:

    - Las clases deben llevar la palabra Test con la T en mayuscula para que funcione
    - Todas las funciones para testear deben llevar la palabra test con la t en minuscula para que funcione
'''

#! Los tests deben realizarse al principio siempre.

'''
Usando el repaso anterior de POO_herencia vamos a hacer tests:
'''

import unittest
from POO_herencia import CuentaCorriente, CajaAhorro

class TestCuentaCorriente(unittest.TestCase):

    def test_cc_deposito(self):
        cuenta_corriente = CuentaCorriente()
        cuenta_corriente.deposito(1000)
        self.assertEqual(cuenta_corriente.saldo_final(), 1000)

    def test_cc_deposito_doble(self):
        cuenta_corriente = CuentaCorriente()
        cuenta_corriente.deposito(1000)
        cuenta_corriente.deposito(1000)
        self.assertEqual(cuenta_corriente.saldo_final(), 2000)

    def test_cc_extraccion(self):
        cuenta_corriente = CuentaCorriente()
        cuenta_corriente.deposito(1000)
        cuenta_corriente.extraccion(500)
        self.assertEqual(cuenta_corriente.saldo_final(), 500)


    def test_cc_extraccion_limite_final(self):
        cuenta_corriente = CuentaCorriente()
        cuenta_corriente.deposito(1000)
        cuenta_corriente.extraccion(2000)
        cuenta_corriente.extraccion(2000)
        cuenta_corriente.extraccion(1000)
        self.assertEqual(cuenta_corriente.saldo_final(), -3000)


class TestCajaAhorro(unittest.TestCase):

    def test_ca_deposito(self):
        caja_ahorro = CajaAhorro()
        caja_ahorro.deposito(1000)
        self.assertEqual(caja_ahorro.saldo_final(), 1000)

    def test_ca_deposito_doble(self):
        caja_ahorro = CajaAhorro()
        caja_ahorro.deposito(1000)
        caja_ahorro.deposito(1000)
        self.assertEqual(caja_ahorro.saldo_final(), 2000)

    def test_ca_extraccion(self):
        caja_ahorro = CajaAhorro()
        caja_ahorro.deposito(1000)
        caja_ahorro.extraccion(500)
        self.assertEqual(caja_ahorro.saldo_final(), 500)

    def test_ca_extraccion_limite(self):
        caja_ahorro = CajaAhorro()
        caja_ahorro.deposito(1000)
        caja_ahorro.extraccion(2000)
        self.assertEqual(caja_ahorro.saldo_final(), 1000)


if __name__ == '__main__':
    unittest.main()