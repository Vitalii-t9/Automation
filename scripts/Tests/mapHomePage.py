import time
import unittest
import sys
import os
from selenium import webdriver
import logging
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from scripts.Pages.homePage import HomePage
from scripts.Pages.cartPage import CartPage
from scripts.Pages.accountPage import AccountPage
from scripts.Pages.contactUsPage import ContactUs
from scripts.Pages.createAnAccountPage import CreateAnAccountPage
from scripts.Pages.signInPage import SignInPage
from scripts.Pages.signOutPage import SignOutPage
from scripts import Utils
from scripts import TestLogging
import HtmlTestRunner

driver_path = Utils.select_webdriver_by_os_and_browser("chromedriver_ga")
fileLogName = os.path.abspath(__file__.replace(".py", ".log"))


if "/" in fileLogName:
    fileLogName = os.path.split(fileLogName)[1]
scriptPath = os.path.abspath(os.path.dirname(__file__))
os.chdir(scriptPath)


class MapHomePage(unittest.TestCase):

    global logger
    logger = TestLogging.create_log_file_handler(os.path.join(scriptPath, TestLogging.cleanupLogFileName(fileLogName)),
                                                 logging.INFO)
    @classmethod
    def setUpClass(cls):
        # os.path.join(__filepath__, "../../driver/webdriver/chromederiver")
        cls.driver = webdriver.Chrome(executable_path=driver_path)
        logger.info(f"Select Web driver: {cls.driver}")
        cls.driver.implicitly_wait(10)
        # cls.driver.maximize_window()

    def test_links_on_hp(self):
        driver = self.driver
        link = 'http://automationpractice.com/index.php'
        driver.get(link)
        logger.info(f"go to the home page {link} ")
        home = HomePage(driver)
        contactUs = ContactUs(driver)
        home.click_on_locator(home.contactUs_link_textlink)
        logger.info("Loading page successful")
        logger.info(f"click on Contact us")
        contactUs.click_on_locator(contactUs.subjectHeading_dropdownmenu_id)
        time.sleep(1)
        contactUs.select_by_visibletext(
            contactUs.subjectHeading_dropdownmenu_id, contactUs.subjectHeading_dropdownmenuitem_visibletext)
        time.sleep(2)
        logger.info("success")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Passed")


if __name__ == "__main__":
    unittest.main()


