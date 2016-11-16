import unittest
import numpy as np

def test_slice(red, orange, green, celeste):
    class MyTest(unittest.TestCase):
    		
        def test_red(self):
            self.assertEqual(red.tolist(), np.array([ 2, 12, 22, 32, 42, 52]).tolist())

        def test_orange(self):
            self.assertEqual(orange.tolist(), np.array([3,4]).tolist())

        def test_green(self):
            self.assertEqual(green.tolist(), np.array([[20, 22, 24],[40, 42, 44]]).tolist())

        def test_celeste(self):
             self.assertEqual(celeste.tolist(), np.array([[44, 45],[54, 55]]).tolist())

    suite = unittest.TestLoader().loadTestsFromTestCase( MyTest )
    unittest.TextTestRunner(verbosity=2).run( suite )