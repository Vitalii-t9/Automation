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


class CreteAnAccountTest(unittest.TestCase):

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


        # Step 2: click on Sign In
        home = HomePage(driver)
        home.click_on_locator(home.signin_link_textlink)
        logger.info("Click on Sign In")

        # Step 3: On the Sign In Page enter email and click create an Account 
        signIn = SignInPage(driver)
        email = "user0987@super.com"
        signIn.enter_text(signIn.emailToCreateAnAccount_textbox_id, email)
        logging.info(f"Enter an email *{email}*")
        signIn.click_on_locator(signIn.createAnAccountSubmitbtn_btn_id)
        logging.info("Click on the create an account btn")

        # Step 4: On the Create An Account Page enter all required data
        creatAccount = CreateAnAccountPage(driver)
        creatAccount.click_on_locator(creatAccount.genderMr_radiobtn_id)
        logger.info("Click on -Mr- radio btn")
        userName = "Name"
        creatAccount.enter_text(creatAccount.userFirstName_textbox_id, userName)
        logger.info("Enter user name")
        userLastName = "LastName"
        creatAccount.enter_text(creatAccount.userSecondName_textbox_id, userLastName)
        logger.info("Enter Last Name")
        creatAccount.enter_text(creatAccount.userEmail_textbox_id, email)
        logger.info("Enter user email")
        creatAccount.enter_text(creatAccount.userPasswd_textbox_id, "1q2W3e4R@")
        logger.info("Enter Password")
        creatAccount.select_by_visibletext(creatAccount.dayOfBirth_dropdownmenu_id, creatAccount.dayOfBirth_menuitem_visibletext)
        logger.info("Select day of Birth")
        creatAccount.select_by_visibletext(creatAccount.monthOfBirth_dropdownmenu_id, creatAccount.monthOfBirth_menuitem_visibletext)
        logger.info("Select month of Birth")
        creatAccount.select_by_visibletext(creatAccount.yearOfBirth_dropdownmenu_id, creatAccount.yearOfBirth_menuitem_visibletext)
        logger.info("Select year of Birth")

        creatAccount.enter_text(creatAccount.firstNameDelivery_textbox_id, userName)
        logger.info("Enter user name for delivery")
        creatAccount.enter_text(creatAccount.lastNameDelivery_textbox_id, userLastName)
        logger.info("Enter user last name for delivery")
        creatAccount.enter_text(creatAccount.companyName_textbox_id, "Company")
        logger.info("Enter company name ")
        creatAccount.enter_text(creatAccount.address_textbox_id, "City, str.Street, a.120")
        logger.info("Enter full address")
        creatAccount.enter_text(creatAccount.addressLine2_textbox_id, "Some city, street, a.125")
        logger.info("Enter second address")
        creatAccount.enter_text(creatAccount.city_textbox_id, "City")
        logger.info("Enter city name")
        creatAccount.select_by_visibletext(creatAccount.state_dropdownmenu_id, creatAccount.state_menuitem_visibletext)
        logger.info("Select state")
        creatAccount.enter_text(creatAccount.postCode_textbox_id, "34563")
        logger.info("Enter Postal Code")
        creatAccount.select_by_visibletext(creatAccount.contry_dropdownmenu_id)
        logger.info("Select country")
        creatAccount.enter_text(creatAccount.additionalInformation_textbox_id, "Some additional information")
        logger.info("Enter some additional information")
        creatAccount.enter_text(creatAccount.mobilePhone_textbox_id, "+380987654327")
        logger.info("Enter phone number")
        creatAccount.enter_text(creatAccount.aliasForAddress_textbox_id, "My address")
        logger.info("Enter alias for address")
        creatAccount.click_on_locator(creatAccount.submitAccount_btn_id)
        logger.info("Click on Submit register Btn")


    @classmethod
    def tearDownClass(cls):
        logger.info("Connection interrupt")
        cls.driver.close()
        logger.info("Close the browsers window")
        cls.driver.quit()
        logger.info("Test Passed")


if __name__ == "__main__":
    unittest.main()


