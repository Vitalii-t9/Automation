import time
import unittest
import sys
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from scripts.Pages.homePage import HomePage
from scripts.Pages.cartPage import CartPage
from scripts.Pages.accountPage import AccountPage
from scripts.Pages.contactUsPage import ContactUs
from scripts.Pages.createAnAccountPage import CreateAnAccountPage
from scripts.Pages.signInPage import SignInPage
from scripts.Pages.signOutPage import SignOutPage
import HtmlTestRunner

class MapHomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../../drivers/chromedriver.exe") # pathfile = os.path.abspath(__file__) ; os.path.join(__filepath__, "../../driver/webdriver/chromederiver")
        cls.driver.implicitly_wait(10)
        # cls.driver.maximize_window()


    def test_links_on_hp(self):
        driver = self.driver
        driver.get('http://automationpractice.com/index.php')

        home = HomePage(driver)
        contactUs = ContactUs(driver)
        home.click_on_locator(home.contactUs_link_textlink)
        contactUs.click_on_locator(contactUs.subjectHeading_dropdownmenu_id)
        contactUs.select_by_visibletext(contactUs.subjectHeading_dropdownmenu_id, contactUs.subjectHeading_dropdownmenuitem_visibletext)
        time.sleep(5)



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Passed")

if __name__ == "__main__":
    unittest.main()


