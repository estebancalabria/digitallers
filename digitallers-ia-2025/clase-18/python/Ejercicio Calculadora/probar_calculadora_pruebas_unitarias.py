import unittest
import calculadora

class TestCalculadora(unittest.TestCase): #Esto es herencia de la clase TestCase de unittest, lo vamos a ver mas adelante   
    def test_sumar(self):
        self.assertEqual(calculadora.sumar(10, 5), 15)
        self.assertEqual(calculadora.sumar(-1, 1), 0)
        self.assertEqual(calculadora.sumar(-1, -1), -2)

    def test_restar(self):
        self.assertEqual(calculadora.restar(10, 5), 5)
        self.assertEqual(calculadora.restar(-1, 1), -2)
        self.assertEqual(calculadora.restar(-1, -1), 0)

    def test_multiplicar(self):
        self.assertEqual(calculadora.multiplicar(10, 5), 50)
        self.assertEqual(calculadora.multiplicar(-1, 1), -1)
        self.assertEqual(calculadora.multiplicar(-1, -1), 1)

    def test_dividir(self):
        self.assertEqual(calculadora.dividir(10, 5), 2)
        self.assertEqual(calculadora.dividir(-10, 5), -2)
        self.assertAlmostEqual(calculadora.dividir(10, 3), 3.333333333333333333)
        with self.assertRaises(ValueError):
            calculadora.dividir(10, 0)

if __name__ == '__main__':
    unittest.main()