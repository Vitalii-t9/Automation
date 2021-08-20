from selenium import webdriver
from scripts.Locators.locators import Locators

class AccountPage():

    def __init__(self, driver):
        self.driver = driver

        self.account_link_xpath = Locators.account_link_xpath
        self.home_link_xpath = Locators.home_link_xpath
        self.orderHistAndAccount_link_xpath = Locators.orderHistAndAccount_link_xpath
        self.myWishList_link_xpath = Locators.myWishList_link_xpath
        self.myCreditSlips_link_xpath = Locators.myCreditSlips_link_xpath
        self.myAddress_link_xpath = Locators.myAddress_link_xpath
        self.myPersonalInfo_link_xpath = Locators.myPersonalInfo_link_xpath

    def click_MyAccount(self):
        self.driver.find_element_by_xpath(self.account_link_xpath).click()

    def click_HomeLink(self):
        self.driver.find_element_by_xpath(self.home_link_xpath).click()

    def click_OrderHistAndAccount(self):
        self.driver.find_element_by_xpath(self.orderHistAndAccount_link_xpath).click()

    def click_MyWishList(self):
        self.driver.find_element_by_xpath(self.myWishList_link_xpath).click()

    def click_MyCreditCardSlips(self):
        self.driver.find_element_by_xpath(self.myCreditSlips_link_xpath).click()

    def click_MyAddressLink(self):
        self.driver.find_element_by_xpath(self.myAddress_link_xpath).click()

    def click_MyPersonInfo(self):
        self.driver.find_element_by_xpath(self.myPersonalInfo_link_xpath).click()