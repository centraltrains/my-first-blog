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
    
    def find_row_in_table(self, text, id):
        table = self.browser.find_element_by_id(id)
        rows = table.find_elements_by_tag_name("tr")
        for row in rows:
            if text in row.text:
                return row

        return None

    def get_link_from_listing(self, text, id):
        row = self.find_row_in_table(text, id)
        if row != None:
            links = row.find_elements_by_tag_name("a")
            for link in links:
                return link.get_attribute("href")
        
        return None


    def test_website_connect(self):

        #Connect to website
        self.browser.get("http://127.0.0.1:8000/admin")
        username = self.browser.find_element_by_id("id_username")
        password = self.browser.find_element_by_id("id_password")
        username.send_keys("test")
        password.send_keys("testworld")
        password.send_keys(Keys.ENTER)
        time.sleep(1)
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

        #Edit
        editLink = self.get_link_from_listing("GCSEs: A*A*A*AABCD", "education-table")
        self.assertIsNotNone(editLink)
        self.browser.get(editLink)

        #Change GCSEs to A*********
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("Edit", header_text)
        editNameInputBox = self.browser.find_element_by_id("input-name")
        editDetailsInputBox = self.browser.find_element_by_id("education-input-details")
        eduNameInputBox.send_keys(Keys.CONTROL, "a")
        eduNameInputBox.send_keys(Keys.BACKSPACE)
        eduNameInputBox.send_keys("GCSEs: A*******")

        #Check edit
        self.browser.get("http://127.0.0.1:8000/cv")
        self.check_text_in_id("GCSEs: A*******", "education-table")

        self.fail("Finish the test")



if __name__ == '__main__':
    unittest.main(warnings="ignore")