import platform
import os
from selenium import webdriver

from selenium.webdriver.android.webdriver import WebDriver


def select_webdriver_by_os_and_browser(driverName):

    osType = platform.system()
    listOfBrowser = ["chrome_beta", "chrome_canary", "chrome_ga", "geko_ga", "msedge_ga"]

    if osType == "Windows":
        winDirName = os.path.abspath("../../drivers/webdrivers_for_win")
        sepDriverName = driverName.replace("driver", "")
        if sepDriverName in listOfBrowser:
            for i in listOfBrowser:
                if i == sepDriverName:
                    absDriverPath = os.path.abspath(winDirName + f"/{driverName}/{driverName.split('_')[0]}.exe")
    if osType == "Darwin" or osType == "Linux":
        macDirName = os.path.abspath("../../drivers/webdrivers_for_mac")
        sepDriverName = driverName.replace("driver", "")
        if sepDriverName in listOfBrowser:
            for i in listOfBrowser:
                if i == sepDriverName:
                    absDriverPath = os.path.abspath(macDirName + f"/{driverName}/{driverName.split('_')[0]}")
                    break

    return absDriverPath

def chooseWebDriver(browserName, driverPath):
    if "chrome" in browserName.lower():
        return webdriver.Chrome(executable_path=driverPath)
    elif "firefox" in browserName.lower():
        return webdriver.Firefox(executable_path=driverPath)
    elif "edge" in browserName.lower():
        return webdriver.Edge(executable_path=driverPath)
    elif "opera" in browserName.lower():
        return webdriver.Opera(executable_path=driverPath)


def setUpTest(logger, browser, driverPath, starUrl):
    driver = chooseWebDriver(browserName=browser, driverPath=driverPath)
    logger.info(f"Select Web driver: {driver} by {browser}")
    driver.implicitly_wait(10)
    logger.info("implicitly wait 10 second")
    driver.maximize_window()
    logger.info("Maximize browser window")
    driver.get(starUrl)
    logger.info(f"go to the start URL {starUrl} ")
    return driver

def finishTest(logger, driver):
    logger.info("Connection interrupt")
    driver.close()
    logger.info("Close the browsers window")
    driver.quit()
    os._exit(0)

def checkCondition(logger, condition, positiveMessage, negativeMessage , driver):
    if condition:
        logger.info(positiveMessage)
    else:
        logger.info(negativeMessage)
        logger.info("Test Failed")
        finishTest(logger, driver)
        


