#Ahora ustedes hace las pruebas unitarias!

import unittest
from validador_cadenas import ValidadorCadenas

class TestValidadorCadenas(unittest.TestCase):
    """
    Clase de pruebas unitarias para la clase ValidadorCadenas.
    """

    def test_es_email(self):
        """
        Pruebas para el método es_email.
        """
        # Casos válidos
        self.assertTrue(ValidadorCadenas.es_email("test@example.com"))
        self.assertTrue(ValidadorCadenas.es_email("usuario.nombre@dominio.co.uk"))
        self.assertTrue(ValidadorCadenas.es_email("primer.apellido@sub.dominio.com"))

        # Casos inválidos
        self.assertFalse(ValidadorCadenas.es_email("correo-invalido"))
        self.assertFalse(ValidadorCadenas.es_email("otro@.com"))
        self.assertFalse(ValidadorCadenas.es_email("usuario@dominio"))
        self.assertFalse(ValidadorCadenas.es_email("@dominio.com"))
        self.assertFalse(ValidadorCadenas.es_email("usuario@dominio.c")) # Dominio muy corto
        #self.assertFalse(ValidadorCadenas.es_email(None)) # No es string
        #self.assertFalse(ValidadorCadenas.es_email(123)) # No es string


    def test_es_url(self):
        """
        Pruebas para el método es_url.
        """
        # Casos válidos
        self.assertTrue(ValidadorCadenas.es_url("https://www.google.com"))
        self.assertTrue(ValidadorCadenas.es_url("http://example.org/path/to/resource?query=1"))
        self.assertTrue(ValidadorCadenas.es_url("www.ejemplo.com/pagina.html"))
        #self.assertTrue(ValidadorCadenas.es_url("ftp://ftp.example.com/file.txt")) # La regex soporta ftp://
        #self.assertTrue(ValidadorCadenas.es_url("http://localhost:8080/")) # Acepta localhost

        # Casos inválidos
        self.assertFalse(ValidadorCadenas.es_url("url-invalida"))
        self.assertFalse(ValidadorCadenas.es_url("http:///nodominio.com"))
        self.assertFalse(ValidadorCadenas.es_url("http://.com"))
        #self.assertFalse(ValidadorCadenas.es_url("solo.com"))
        #self.assertFalse(ValidadorCadenas.es_url(None)) # No es string
        #self.assertFalse(ValidadorCadenas.es_url(123)) # No es string


    def test_es_numero_entero(self):
        """
        Pruebas para el método es_numero_entero.
        """
        # Casos válidos
        self.assertTrue(ValidadorCadenas.es_numero_entero("123"))
        self.assertTrue(ValidadorCadenas.es_numero_entero("-45"))
        self.assertTrue(ValidadorCadenas.es_numero_entero("0"))
        self.assertTrue(ValidadorCadenas.es_numero_entero("1234567890"))

        # Casos inválidos
        self.assertFalse(ValidadorCadenas.es_numero_entero("123.45")) # Decimal
        self.assertFalse(ValidadorCadenas.es_numero_entero("abc")) # Letras
        self.assertFalse(ValidadorCadenas.es_numero_entero("")) # Cadena vacía
        self.assertFalse(ValidadorCadenas.es_numero_entero("10a")) # Alfanumérico
        #self.assertFalse(ValidadorCadenas.es_numero_entero(None)) # No es string
        #self.assertFalse(ValidadorCadenas.es_numero_entero(123)) # Es int, no string


    def test_longitud_valida(self):
        """
        Pruebas para el método longitud_valida.
        """
        # Casos válidos
        self.assertTrue(ValidadorCadenas.longitud_valida("hola", 2, 5))  # Longitud 4, dentro de [2, 5]
        self.assertTrue(ValidadorCadenas.longitud_valida("ab", 2, 5))    # Longitud 2, límite inferior
        self.assertTrue(ValidadorCadenas.longitud_valida("abcde", 2, 5)) # Longitud 5, límite superior
        self.assertTrue(ValidadorCadenas.longitud_valida("", 0, 5))     # Longitud 0, límite inferior

        # Casos inválidos
        self.assertFalse(ValidadorCadenas.longitud_valida("a", 2, 5))       # Longitud 1, menor que min
        self.assertFalse(ValidadorCadenas.longitud_valida("abcdefg", 2, 5)) # Longitud 7, mayor que max
        self.assertFalse(ValidadorCadenas.longitud_valida("", 1, 5))        # Longitud 0, menor que min
        #self.assertFalse(ValidadorCadenas.longitud_valida(None, 0, 5))      # No es string
        #self.assertFalse(ValidadorCadenas.longitud_valida(123, 0, 5))       # No es string
        #self.assertFalse(ValidadorCadenas.longitud_valida([], 0, 5))        # No es string


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False) # Agregamos argv y exit para que funcione bien en VS Code si lo ejecutas varias veces.