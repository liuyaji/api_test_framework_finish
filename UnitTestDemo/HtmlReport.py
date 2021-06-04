import unittest
from HTMLTestRunner import HTMLTestRunner
from UnitTestDemo.test_mathfunc import TestMathFunc

if __name__ == "__main__":
    suite = unittest.TestSuite()
    # 执行加法、减法、除法
    tests = [TestMathFunc("test_add"), TestMathFunc("test_divide"),
             TestMathFunc("test_minus")]
    suite.addTests(tests)
    # addTest，添加单个TestCase
    # suite.addTest(TestMathFunc("test_multi"))
    f = open("d:\\reporter.xhtml", "wb")
    runner = HTMLTestRunner(stream=f, title="测试报告",description="测试用例执行情况")
    runner.run(suite)