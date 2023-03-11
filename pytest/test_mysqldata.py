import pytest


def test_register(db):

    cursor = db.cursor()
    cursor.execute("SELECT NAME FROM T_ORG WHERE ID = 1")
    result = cursor.fetchone()
    print(result)
    assert result is not None
    assert result[1] == '人员机构'
    assert result[2] == 'password'


if __name__ == '__main__':
    pytest.main()
