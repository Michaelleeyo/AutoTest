from calculator import Calculator


def test_add():
    c = Calculator(3, 5)
    result = c.add()
    assert result == 8, '加法运算失败'


def test_sub():
    d = Calculator(10, 2)
    result = d.sub()
    assert result == 9, '减法运算失败'


def test_mul():
    e = Calculator(3, 7)
    result = e.mul()
    assert result == 21, '乘法运算失败'


def test_div():
    f = Calculator(9, 3)
    result = f.div()
    assert result == 3, '除法运算失败'


if __name__ == '__main__':
    test_add()
    test_sub()
    test_mul()
    test_div()
