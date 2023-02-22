import pytest


@pytest.fixture
def first_entry():
    return "a"


@pytest.fixture
def order(first_entry):
    return [first_entry]


@pytest.fixture
def second_entry():
    return ["a", 1]


@pytest.fixture
def third_entry():
    return 8


'''可以一次请求多个fixture;
数组A/B的元素插入数组C,可以直接[*A,*B]'''


@pytest.fixture
def order2(second_entry, third_entry):
    return [*second_entry, third_entry]


def test_string(order):
    order.append("b")
    assert order == ["a", "c"]


def test_int(order):
    order.append(2)
    assert order == ["a", 2]


@pytest.fixture
def expected_list():
    return ["a", 1, 8, 6.0]


print(order2)

# 判断order2和expected_list是否相等


def test_expected_list(order2, expected_list):
    order2.append(6.0)
    # print(order2)
    assert order2 == expected_list


''' 一个fixture也可以被多次请求(结果会存储缓存);
my_fixture fixture 被设置为 autouse=True，它将在所有测试用例中自动使用。
无需在测试用例中明确调用 my_fixture 函数，fixture 函数会在测试用例执行前自动运行，并在测试用例执行后自动清理。
'''


@pytest.fixture(autouse=True)
def order3(first_entry, second_entry, third_entry):
    return[first_entry, *second_entry, third_entry]


def test_expected_list2(order3, expected_list):
    assert order3 == expected_list
