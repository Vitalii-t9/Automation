from scripts.Locators.locators import Locators


class SignInPage():

    def __init__(self, driver):
        self.driver = driver

        self.emailToCreateAnAccount_textbox_id = Locators.emailToCreateAnAccount_textbox_id
        self.createAnAccountSubmitbtn_btn_id = Locators.createAnAccountSubmitbtn_btn_id
        self.emailToSignIn_textbox_id = Locators.emailToSignIn_textbox_id
        self.passwdToSignIn_textbox_id = Locators.passwdToSignIn_textbox_id
        self.forgotPasswd_link_textlink = Locators.forgotPasswd_link_textlink
        self.submitLogin_btn_id = Locators.submitLogin_btn_id

    def enter_EmailCreat(self, email):
        self.driver.find_element_by_link_text(self.emailToCreateAnAccount_textbox_id).send_keys(email)

    def click_SubBtnCrtAcount(self):
        self.driver.find_element_by_id(self.createAnAccountSubmitbtn_btn_id).click()

    def enter_EmailToSignIn(self, email):
        self.driver.find_element_by_id(self.emailToSignIn_textbox_id).send_keys(email)

    def enter_PasswToSignIn(self, password):
        self.driver.find_element_by_id(self.passwdToSignIn_textbox_id).send_keys(password)

    def click_On_ForgPassw(self):
        self.driver.find_element_by_link_text(self.forgotPasswd_link_textlink).click()

    def click_SubLoginBtn(self):
        self.driver.find_element_by_id(self.submitLogin_btn_id).click()

