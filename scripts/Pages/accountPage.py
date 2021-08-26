from scripts.Locators.accountPage import AccountPageLocators
from scripts.functions import Action

class AccountPage(Action):

    def __init__(self, driver):
        self.driver = driver

        self.account_link_xpath = AccountPageLocators.account_link_xpath
        self.home_link_xpath = AccountPageLocators.home_link_xpath
        self.orderHistAndAccount_link_xpath = AccountPageLocators.orderHistAndAccount_link_xpath
        self.myWishList_link_xpath = AccountPageLocators.myWishList_link_xpath
        self.myCreditSlips_link_xpath = AccountPageLocators.myCreditSlips_link_xpath
        self.myAddress_link_xpath = AccountPageLocators.myAddress_link_xpath
        self.myPersonalInfo_link_xpath = AccountPageLocators.myPersonalInfo_link_xpath








