from baidu_page import BaiduPage
import unittest
from selenium import webdriver
from time import sleep


class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def test_baidu_search_case1(self):
        page = BaiduPage(self.driver)
        page.get("https://www.baidu.com")
        sleep(3)
        page.search_input = "selenium"
        page.search_button.click()
        sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
