pytest

1.断言
python自带的assert
2.Fixture
@pytest.fixture()
通常用来对测试方法、测试函数、测试类和整个测试文件进行初始化或还原测试环境
setup_module/teardown_module 当前文件中，在所有cesium用例执行前后执行
setup_function/teardown_function 测试函数前后执行
setup/teardown 测试函数前后执行。也适用于类方法
例：
# 功能函数
def multiply(a, b):
return a * b
class TestMultiply:
# =====Fixture========
@classmethod
def setup_class(cls):
print("setup_class=========>")
@classmethod
def teardown_class(cls):
print("teardown_class=========>")
def setup_method(self, method):
print("setup_method----->>")
def teardown_method(self, method):
print("teardown_method-->>")
def setup(self):
print("setup----->") 
def teardown(self):
print("teardown-->")
# =====测试用例========
def test_numbers_5_6(self):
print('test_numbers_5_6')
assert multiply(5, 6) == 30
def test_strings_b_2(self):
print('test_strings_b_2')
assert multiply('b', 2) == 'bb' 
3.参数化
@pytest.mark.parametrize(argnames,argvalues,indirect=False,ids=None,scope=None)
argnames参数名必填，argvalues参数对应值，一般使用list
例：
import pytest
import math
# pytest 参数化
@pytest.mark.parametrize(
"base, exponent, expected",
[(2, 2, 4),
(2, 3, 8),
(1, 9, 1),
(0, 9, 0)],
ids=["case1", "case2", "case3", "case4"]
)
def test_pow(base, exponent, expected):
assert math.pow(base, exponent) == expected 
4.跳过测试函数
在需要跳过的测试脚本之上加上装饰器@pytest.mark.skipif(condition,reason="xxx")
condition跳过的条件，必传；reason标注原因，必传
测试脚本前加入@pytest.mark.skip()
5..预期失败
@pytest.mark.xfail(condition=None,reason=None,raises=None,run=True,strict=False)
condition跳过的条件，必传；reason标注原因，必传

