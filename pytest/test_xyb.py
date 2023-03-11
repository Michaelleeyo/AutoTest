import requests
import pytest

# 登录


def login():
    r = requests.get('https://xyb.xhu.edu.cn/api/v1/us?t=0720170020')
    print(r.status_code)
    cookies = r.request.prepare_cookies
    return cookies


login()
