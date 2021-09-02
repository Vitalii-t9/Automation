from scripts.Locators.signOutPage import SignOutPageLocators
from scripts.Actions import Action


class SignOutPage(Action):

    def __init__(self, driver):
        self.driver = driver
        self.singOut_link_textlink = SignOutPageLocators.singOut_link_textlink


