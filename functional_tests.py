from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class SiteTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    #def tearDown(self):
        #self.browser.quit()

    def check_text_in_id(self, text, id):
        table = self.browser.find_element_by_id(id)
        rows = table.find_elements_by_tag_name("tr")
        self.assertIn(text, table.text)

    def test_website_connect(self):

        #Connect to website
        self.browser.get("http://127.0.0.1:8000/admin")
        time.sleep(10)
        self.browser.get("http://127.0.0.1:8000/cv")

        #Check it is the right website
        self.assertIn("CV", self.browser.title)

        #Find an input box for education
        eduNameInputBox = self.browser.find_element_by_id("education-input-name")
        eduDetailsInputBox = self.browser.find_element_by_id("education-input-details")
        eduStartInputBox = self.browser.find_element_by_id("education-input-start")
        eduEndInputBox = self.browser.find_element_by_id("education-input-end")

        #Add a new education event
        eduNameInputBox.send_keys("St George's")
        eduDetailsInputBox.send_keys("GCSEs: A*A*A*AABCD")
        eduEndInputBox.send_keys("2017-01-01")
        eduStartInputBox.send_keys("2017-01-01")
        #Send
        eduNameInputBox.send_keys(Keys.ENTER)
        time.sleep(1)

        #Check
        self.check_text_in_id("GCSEs: A*A*A*AABCD", "education-table")

        self.fail("Finish the test")



if __name__ == '__main__':
    unittest.main(warnings="ignore")