import pytest
import math

# pytest参数化,和unittest类似，用pytest.mark.parametrize()方法设置参数
# "base,exponent,expected"用来定义参数的名称。ids参数默认为None，用于定义测试用例的名称
# math模块中的pow()用来计算次幂的值，x的y次方


@pytest.mark.parametrize(
    "base,exponent,expected",
    [(2, 2, 4),
     (3, 3, 8),
     (4, 4, 13)],
    ids=["case1", "case2", "case3"]
)
def test_pow(base, exponent, expected):
    assert math.pow(base, exponent) == expected


if __name__ == "__main__":
    pytest.main()
