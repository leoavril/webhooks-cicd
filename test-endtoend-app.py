import unittest
from flask import request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from app import app


class TestAppE2E(unittest.TestCase):
    def setUp(self):
        # Launch your flask app first

        chrome_options = Options()
        chrome_options.binary_location = 'C:\\Users\\Léo\\Documents\\EFREI\\M2\\S9\\ML In Prod\\testinglab\\chrome-win64'
        self.driver = webdriver.Chrome()
        self.driver.get('https://0329-77-141-190-172.ngrok-free.app/')

    def test_add_and_delete_item(self):
        # you can use the driver to find elements in the page
        # example:
        input_field = self.driver.find_element(By.NAME, 'item')
        # this refers to the 'name="item"' attribute of the html element
        # checkout the rest of the methods in the documentation:
        # https://selenium-python.readthedocs.io/locating-elements.html

        # after you select your element, you can send it a key press:
        input_field.send_keys('New E2E Item')
        input_field.send_keys(Keys.RETURN)

        # and you can use the rest of the assetion methods as well:
        self.assertIn('New E2E Item', self.driver.page_source)

        # Testing Update operation
        update_form = self.driver.find_element(By.NAME, 'new_item')
        update_form.send_keys('Updated E2E Item'+Keys.RETURN)
        self.assertIn('Updated E2E Item', self.driver.page_source)
        self.assertNotIn('New E2E Item', self.driver.page_source)

        # Testing Delete operation
        delete_item = self.driver.find_element(By.LINK_TEXT, 'Delete')
        delete_item.click()
        self.assertNotIn('New E2E Item', self.driver.page_source)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
