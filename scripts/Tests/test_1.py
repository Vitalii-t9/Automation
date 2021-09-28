import time
import unittest
import sys
import os
from selenium import webdriver
import logging

from selenium.webdriver.common.by import By
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

logger = TestLogging.create_log_file_handler(os.path.join(scriptPath, TestLogging.cleanupLogFileName(fileLogName)),
                                                logging.INFO)
browser = "Chrome"
startUrl = "http://automationpractice.com/index.php"

# Step 1 Set up general config and go to the start Page 
driver = Utils.setUpTest(logger, browser, driverPath=driver_path, starUrl=startUrl)
 

def test_SearchBox():
     # Step 2: enter some query to the search box
    
    home = HomePage(driver)
    query = "dress"
    Utils.checkCondition(logger, home.enter_text(logger, home.search_textbox_id, query),
                         f"query '{query}' was entered in the searchBox successful",
                         f"query '{query}' was not entered in the searchBox - failed", driver)


    # Step 3: click on the search button
    Utils.checkCondition(logger, home.click_on_locator(logger, home.submitSerch_Btn_name),
                         f"click search Btn successful",
                         f"click search Btn failed", driver)
    time.sleep(3)


test_SearchBox()


logger.info("Test Passed")
Utils.finishTest(logger, driver)


if __name__ == "__main__":
    unittest.main()


