from scripts.Locators.signOutPage import SignOutPageLocators

class SignOutPage():

    def __init__(self, driver):
        self.driver = driver
        self.singOut_link_textlink = SignOutPageLocators.singOut_link_textlink


