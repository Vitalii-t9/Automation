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


class SendMessageOnContactsUsPageTest(unittest.TestCase):

    global logger
    logger = TestLogging.create_log_file_handler(os.path.join(scriptPath, TestLogging.cleanupLogFileName(fileLogName)),
                                                 logging.INFO)
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=driver_path)
        logger.info(f"Select Web driver: {cls.driver}")
        cls.driver.implicitly_wait(10)
        logger.info("implicitly wait 10 second")
        cls.driver.maximize_window()
        logger.info("Maximize browser window")

    def test_search_line(self):
        driver = self.driver
        logger.info(f"Driver is {driver}")
        link = 'http://automationpractice.com/index.php'
        logger.info(f"Test will start from {link} address")

        # Step 1: go to the home page
        driver.get(link)
        logger.info(f"go to the home page {link} ")


        # Step 2: click on Contact Us
        home = HomePage(driver)
        home.click_on_locator(home.contactUs_link_linktext)
        logger.info("Click on the Contact Us")

        # Step 3: in the Contact Us Page enter all data and send message
        contact = ContactUs(driver)
        contact.select_by_visibletext(contact.subjectHeading_dropdownmenu_id, contact.subjectHeading_dropdownmenuitem_visibletext)
        logger.info("Select item from Subject Heading")
        contact.enter_text(contact.email_textbox_id, "12test@goo.com")
        logger.info("Enter test email")
        time.sleep(3)
        contact.enter_text(contact.orderReference_textbox_id, "Test text")
        logger.info("Enter order reference")
        contact.enter_text(contact.message_textbox_id, "Here is some test text")
        contact.click_on_locator(contact.send_btn_xpath)
        logger.info("click on the Send btn")
        time.sleep(5)




    @classmethod
    def tearDownClass(cls):
        logger.info("Connection interrupt")
        cls.driver.close()
        logger.info("Close the browsers window")
        cls.driver.quit()
        logger.info("Test Passed")


if __name__ == "__main__":
    unittest.main()


