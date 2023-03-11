import smtplib
import pytest
import pymysql


@pytest.fixture(scope="module")
def smtp_connection():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)


@pytest.fixture(scope='session')
def db():
    try:
        conn = pymysql.connect(host='170.18.10.148', user='root',
                               password='Sudy.web123', database='Coreplus4', port=3010)
        yield conn
        conn.close()
    except:
        print('连接失败')
