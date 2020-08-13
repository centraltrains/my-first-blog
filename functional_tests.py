from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class SiteTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

        #Login
        self.browser.get("http://127.0.0.1:8000/admin")
        username = self.browser.find_element_by_id("id_username")
        password = self.browser.find_element_by_id("id_password")
        username.send_keys("test")
        password.send_keys("testworld")
        password.send_keys(Keys.ENTER)
        time.sleep(1)

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

    def inital_tests(self):
        self.browser.get("http://127.0.0.1:8000/cv")
        #Check it is the right website
        self.assertIn("CV", self.browser.title)

    
    def add_record(self, testScope, dataToInput, checkField):
        self.browser.get("http://127.0.0.1:8000/cv")

        #Add data into fields
        for k, v in dataToInput.items():
            inputBox = self.browser.find_element_by_id(testScope + "-input-" + k)
            inputBox.send_keys(v)


        saveButton = self.browser.find_element_by_id(testScope + "-save")
        saveButton.click()
        time.sleep(1)

        #Check
        
        self.check_text_in_id(dataToInput[checkField], testScope + "-table")

    def edit_record(self, testScope, getTerm, editData, checkField):
         #Edit
        editLink = self.get_link_from_listing(getTerm, testScope + "-table")
        self.assertIsNotNone(editLink)
        self.browser.get(editLink)

        #Replace terms
        for k, v in editData.items():
            inputBox = self.browser.find_element_by_id("input-" + k)
            inputBox.send_keys(Keys.CONTROL, "a")
            inputBox.send_keys(Keys.BACKSPACE)
            inputBox.send_keys(v)

        
        saveButton = self.browser.find_element_by_id("save")
        saveButton.click()


        time.sleep(1)

        #Check edit
        self.browser.get("http://127.0.0.1:8000/cv")
        self.check_text_in_id(editData[checkField], testScope + "-table")

    def delete_record(self, testScope, getTerm):
        ##Find to edit again
        editLink = self.get_link_from_listing(getTerm, testScope + "-table")
        self.assertIsNotNone(editLink)
        self.browser.get(editLink)
        
        #Delete
        deleteButton = self.browser.find_element_by_id("delete-button")
        link = deleteButton.find_elements_by_tag_name("a")
        deleteUrl = link[0].get_attribute("href")
        self.browser.get(deleteUrl)

        #Check Delete
        self.browser.get("http://127.0.0.1:8000/cv")
        editLink = self.get_link_from_listing(getTerm, testScope + "-table")
        self.assertIsNone(editLink)

    def test_education_add(self):

        self.inital_tests()

        self.add_record("education", {"name" : "St George's", "details" : "GCSEs: A*A*A*AABCD", "start" : "2017-01-01", "end" : "2017-01-01"}, "details")
        self.edit_record("education", "GCSEs: A*A*A*AABCD", {"details" : "GCSEs: A*******"}, "details")
        self.delete_record("education", "GCSEs: A*******")

        self.add_record("headInfo", {"details" : "Benjamin Roughtoon",}, "details")
        self.edit_record("headInfo", "Benjamin Roughtoon", {"details" : "Benjamin Roughton"}, "details")
        self.delete_record("headInfo", "Benjamin Roughton")

        self.add_record("work", {"name" : "Nowhere Ltd", "details" : "Nothing", "start" : "1999-01-01", "end" : "2020-01-01"}, "details")
        self.edit_record("work", "Nothing", {"details" : "Still Nothing"}, "details")
        self.delete_record("work", "Still Nothing")

        self.add_record("projects", {"name" : "Bloxy Bingo", "details" : "nothing", "start" : "2020-06-01", "end" : "2020-08-01"}, "details")
        self.edit_record("projects", "nothing", {"details" : "Roblox Game lockdown project! yay!"}, "details")
        self.delete_record("projects", "Roblox Game lockdown project! yay!")



        self.fail("Finish the test")


if __name__ == '__main__':
    unittest.main(warnings="ignore")