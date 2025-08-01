import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase): #Esto es herencia de la clase TestCase de unittest, lo vamos a ver mas adelante   
    def test_sumar(self):
        self.assertEqual(Calculadora.sumar(10, 5), 15)
        self.assertEqual(Calculadora.sumar(-1, 1), 0)
        self.assertEqual(Calculadora.sumar(-1, -1), -2)

    def test_restar(self):
        self.assertEqual(Calculadora.restar(10, 5), 5)
        self.assertEqual(Calculadora.restar(-1, 1), -2)
        self.assertEqual(Calculadora.restar(-1, -1), 0)

    def test_multiplicar(self):
        self.assertEqual(Calculadora.multiplicar(10, 5), 50)
        self.assertEqual(Calculadora.multiplicar(-1, 1), -1)
        self.assertEqual(Calculadora.multiplicar(-1, -1), 1)

    def test_dividir(self):
        self.assertEqual(Calculadora.dividir(10, 5), 2)
        self.assertEqual(Calculadora.dividir(-10, 5), -2)
        self.assertAlmostEqual(Calculadora.dividir(10, 3), 3.3333333333333335)
        with self.assertRaises(ValueError):
            Calculadora.dividir(10, 0)

if __name__ == '__main__':
    unittest.main()