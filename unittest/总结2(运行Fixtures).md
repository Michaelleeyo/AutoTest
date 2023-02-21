unittest

执行多个测试文件
TestLoader类提供了discover()方法从多个文件查找测试用例
discover(start_dir， pattern='test*.py'， top_level_dir=None)
例：
import unittest
# 定义测试用例的目录为当前目录中的 test_case/目录
test_dir = './test_case'
suits = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
if __name__ == '__main__':
runner = unittest.TextTestRunner()
runner.run(suits) 
main()、discover()会更加文件名称确定执行顺序

跳过测试和预期失败
unittest.skip(reason)
unittest.skipIf(condition,reason)
unittest.skipUnless(condition,reason)
unittest.expectedFailure()
例：
import unittest
class MyTest(unittest.TestCase):
@unittest.skip("直接跳过测试")
def test_skip(self):
print("test aaa")
@unittest.skipIf(3 > 2, "当条件为真时跳过测试") 
def test_skip_if(self):
print('test bbb')
@unittest.skipUnless(3 > 2, "当条件为真时执行测试")
def test_skip_unless(self):
print('test ccc')
@unittest.expectedFailure
def test_expected_failure(self):
self.assertEqual(2, 3)
if __name__ == '__main__':
unittest.main() 

Fixture
setUpModule/tearDownModule 整个模块开始和结束时执行
setUpClass/tearDownClass  测试类开始和结束时执行
setUp/tearDown  测试用例开始和结束时直线
setUpClass/tearDownClass 需要通过@classmethod进行装饰，方法的参数为cls
例：
import unittest
def setUpModule():
print("test module start >>>>>>>>>>>>>>")
def tearDownModule():
print("test module end >>>>>>>>>>>>>>")
class MyTest(unittest.TestCase):
@classmethod
def setUpClass(cls):
print("test class start =======>")
@classmethod
def tearDownClass(cls):
print("test class end =======>")
def setUp(self):
print("test case start -->")
def tearDown(self):
print("test case end -->")
def test_case1(self):
print("test case1")
def test_case2(self):
print("test case2")
if __name__ == '__main__':
unittest.main() 

因为为unittest默认根据ASCI码的顺序加载测试用例的(数字与字母的顺序为0~9,A~Z，
a~z)，所以TestAdd 类会优先于 TestBdd 类被执行，test aaa(方法会优先于 test ccc()方法
被执行，也就是说，它并不是按照测试用例的创建顺序从上到下执行的。

我们可以声明测试套件 TestSuite 类，通过addTestO方法按照一定的顺序来加载测试用例。
