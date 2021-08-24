from scripts.Locators.signInPage import SignInPageLocators


class SignInPage():

    def __init__(self, driver):
        self.driver = driver

        self.emailToCreateAnAccount_textbox_id = SignInPageLocators.emailToCreateAnAccount_textbox_id
        self.createAnAccountSubmitbtn_btn_id = SignInPageLocators.createAnAccountSubmitbtn_btn_id
        self.emailToSignIn_textbox_id = SignInPageLocators.emailToSignIn_textbox_id
        self.passwdToSignIn_textbox_id = SignInPageLocators.passwdToSignIn_textbox_id
        self.forgotPasswd_link_textlink = SignInPageLocators.forgotPasswd_link_textlink
        self.submitLogin_btn_id = SignInPageLocators.submitLogin_btn_id


