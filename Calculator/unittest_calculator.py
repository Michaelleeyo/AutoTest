import unittest
from calculator import Calculator
'''unittest规则：
1）创建测试类，必须继承unittest.TestCase
2）创建一个测试方法，必须以test开头
测试方法：
1）创建测试类，传入初始化数据
2）调用测试方法，通过unittest提供的assertEqual()方法来断言
3）最后用main()方法来执行测试用例
'''


class testCalculator(unittest.TestCase):
    def test_add(self):
        c = Calculator(3, 5)
        result = c.add()
        self.assertEqual(result, 8)

    def test_sub(self):
        c = Calculator(7, 5)
        result = c.sub()
        self.assertEqual(result, 2)

    def test_mul(self):
        c = Calculator(3, 5)
        result = c.mul()
        self.assertEqual(result, 9)

    def test_div(self):
        c = Calculator(15, 5)
        result = c.div()
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
