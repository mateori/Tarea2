import unittest

class MyTestCase(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(2 + 2, 4)  # Prueba que pasa

    def test_multiply(self):
        self.assertEqual(3 * 3, 9)  # Prueba que pasa
        
    def test_multiply(self):
        self.assertEqual(10 * 9, 90)  # Prueba que pasa
        
    def test_multiply(self):
        self.assertEqual(7 * 3, 21)  # Prueba que pasa
        
    def test_multiply(self):
        self.assertEqual(6 * 3, 18)  # Prueba que pasa

    def test_subtract(self):
        self.assertEqual(5 - 3, 1)  # Prueba que falla

    def test_divide(self):
        self.assertEqual(10 / 2, 12)  # Prueba que falla
        
    def test_divide(self):
        self.assertEqual(10 / 1, 12)  # Prueba que falla
        
    def test_divide(self):
        self.assertEqual(10 - 2, 3)  # Prueba que falla
    
    def test_divide(self):
        self.assertEqual(10 * 2, 5)  # Prueba que falla

if __name__ == '__main__':
    unittest.main()