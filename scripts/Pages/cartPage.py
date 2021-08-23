from scripts.Locators.cartPage import CartPageLocators
from scripts.functions import Click

class CartPage(Click):

    def __init__(self, driver):
        self.driver = driver

        self.home_link_xpath = CartPageLocators.home_link_xpath
        self.qtyItemPlus_link_selector = CartPageLocators.qtyItemPlus_link_selector
        self.qtyItemMinus_link_xpath = CartPageLocators.qtyItemMinus_link_xpath
        self.removeItem_btn_selector = CartPageLocators.removeItem_btn_selector
        self.continueShop_link_textlink = CartPageLocators.continueShop_link_textlink
        self.proceedToCheckout_link_textlink = CartPageLocators.proceedToCheckout_link_textlink
        self.prodDetView_link_xpath = CartPageLocators.prodDetView_link_xpath

