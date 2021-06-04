import unittest
from UnitTestDemo.test_mathfunc import TestMathFunc

if __name__ == "__main__":
    suite = unittest.TestSuite()

    tests = [TestMathFunc("test_add"),TestMathFunc("test_divide"),TestMathFunc("test_minus")]
    suite.addTests(tests)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)