import time
import unittest
import sys
import os
from selenium import webdriver
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from scripts.Pages.homePage import HomePage
import HtmlTestRunner

class MapHomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/vitalii.titov/PycharmProjects/automationtests/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        # cls.driver.maximize_window()

    def test_links_on_hp(self):
        driver = self.driver
        driver.get('http://automationpractice.com/index.php')

        home = HomePage(driver)
        home.search("dresses")
        time.sleep(6)
        home.click_signIn()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Passed")

if __name__ == "__main__":
    unittest.main()


