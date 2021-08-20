from selenium import webdriver
from scripts.Locators.locators import Locators

class CartPage():

    def __init__(self, driver):
        self.driver = driver

        self.home_link_xpath = Locators.home_link_xpath
        self.qtyItemPlus_link_selector = Locators.qtyItemPlus_link_selector
        self.qtyItemMinus_link_xpath = Locators.qtyItemMinus_link_xpath
        self.removeItem_btn_selector = Locators.removeItem_btn_selector
        self.continueShop_link_textlink = Locators.continueShop_link_textlink
        self.proceedToCheckout_link_textlink = Locators.proceedToCheckout_link_textlink
        self.prodDetView_link_xpath = Locators.prodDetView_link_xpath

    def click_Home(self):
        self.driver.find_element_by_xpath(self.home_link_xpath).click()

    def click_QtyPlus(self):
        self.driver.find_element_by_class_name(self.qtyItemPlus_link_selector).click()

    def click_QtyMinus(self):
        self.driver.find_element_by_xpath(self.qtyItemMinus_link_xpath).click()

    def click_removeItem(self):
        self.driver.find_element_by_css_selector(self.removeItem_btn_selector).click()

    def click_ContinueShop(self):
        self.driver.find_element_by_link_text(self.continueShop_link_textlink).click()

    def click_ProceedToCheckout(self):
        self.driver.find_element_by_link_text(self.proceedToCheckout_link_textlink).click()

    def click_OnProdDetView(self):
        self.driver.find_element_by_link_text(self.prodDetView_link_xpath).click()