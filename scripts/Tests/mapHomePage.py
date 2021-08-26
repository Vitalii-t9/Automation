import time
import unittest
import sys
import os
from selenium import webdriver
import logging
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

fileLogName = os.path.abspath(__file__.replace(".py", ".log"))

if "/" in fileLogName:
    fileLogName = os.path.split(fileLogName)[1]

driver_path = os.path.abspath("../../drivers/chromedriver.exe")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s:%(name)s:%(message)s")

file_handler = logging.FileHandler(fileLogName)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)



class MapHomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # os.path.join(__filepath__, "../../driver/webdriver/chromederiver")
        cls.driver = webdriver.Chrome(executable_path=driver_path)
        cls.driver.implicitly_wait(10)
        # cls.driver.maximize_window()

    def test_links_on_hp(self):
        driver = self.driver
        driver.get('http://automationpractice.com/index.php')

        home = HomePage(driver)
        contactUs = ContactUs(driver)
        home.click_on_locator(home.contactUs_link_textlink)
        contactUs.click_on_locator(contactUs.subjectHeading_dropdownmenu_id)
        time.sleep(1)
        contactUs.select_by_visibletext(
            contactUs.subjectHeading_dropdownmenu_id, contactUs.subjectHeading_dropdownmenuitem_visibletext)
        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Passed")


if __name__ == "__main__":
    unittest.main()


