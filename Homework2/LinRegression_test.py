import unittest
import numpy as np

from LinRegression import *

class LinRegTest(unittest.TestCase):

    def test_Raising(self):
        with self.assertRaises(AttributeError):
            LinearRegressor(self)

    def test_string(self):
        a = np.array([1,2,3,4,5,6,7,8,9,10,'string'])
        b = np.random.randint(15, size=(15, 2))
        with self.assertRaises(AttributeError):
            LinearRegressor(a,b)

if __name__ == "__main__":
    unittest.main()