import pytest


def multiply(a, b):
    return a * b

# ======Fixture===========


def setup_module(module):
    print("=======setup_module=========")


def teardown_module(module):
    print("=======teardown_module=====")


def setup_function(function):
    print("setup_function----->")


def teatdown_function(function):
    print("teardown_function----->")


def setup():
    print("setup---->")


def teardown():
    print("teardown--->")

# 测试用例


def test_multiply_3_4():
    print("测试结果是："+str(multiply(3, 4)))
    assert multiply(3, 4) == 12


def test_multiply_3_a():
    print("测试结果是："+multiply(3, 'a'))
    assert multiply(3, 'a') == 'aaaa'


if __name__ == "__main__":
    pytest.main()
