import pytest


def add(a, b):
    return a + b

# 判断是否为素数


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        return True


def test_add():
    assert add(7, 8) == 14


def test_is_prime():
    assert is_prime(13)
    assert is_prime(7) is False


if __name__ == "__main__":
    pytest.main()
