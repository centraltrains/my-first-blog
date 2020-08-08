from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class SiteTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_website_connect(self):

        #Connect to website
        self.browser.get("http://127.0.0.1:8000/cv")




if __name__ == '__main__':
    unittest.main(warnings="ignore")