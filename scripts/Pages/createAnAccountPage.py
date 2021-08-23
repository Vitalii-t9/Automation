from scripts.Locators.createAnAccountPage import CreateAnAccountPageLocators
from selenium.webdriver.support.ui import Select
from selenium import webdriver
class CreateAnAccountPage():

    def __init__(self, driver):
        self.driver = driver

        self.genderMr_radiobtn_id = CreateAnAccountPageLocators.genderMr_radiobtn_id
        self.genderMrs_radiobtn_id = CreateAnAccountPageLocators.genderMrs_radiobtn_id
        self.userFirstName_textbox_id = CreateAnAccountPageLocators.userFirstName_textbox_id
        self.userSecondName_textbox_id = CreateAnAccountPageLocators.userSecondName_textbox_id
        self.userEmail_textbox_id = CreateAnAccountPageLocators.userEmail_textbox_id
        self.userPasswd_textbox_id = CreateAnAccountPageLocators.userPasswd_textbox_id
        self.dayOfBirth_dropdownmenu_id = CreateAnAccountPageLocators.dayOfBirth_dropdownmenu_id
        self.dayOfBirth_menuitem_visibletext = CreateAnAccountPageLocators.dayOfBirth_menuitem_visibletext
        self.monthOfBirth_dropdownmenu_id = CreateAnAccountPageLocators.monthOfBirth_dropdownmenu_id
        self.monthOfBirth_menuitem_visibletext = CreateAnAccountPageLocators.monthOfBirth_menuitem_visibletext
        self.yearOfBirth_dropdownmenu_id = CreateAnAccountPageLocators.yearOfBirth_dropdownmenu_id
        self.yearOfBirth_menuitem_visibletext = CreateAnAccountPageLocators.yearOfBirth_menuitem_visibletext
        self.receiveNewsletter_checkbox_id = CreateAnAccountPageLocators.receiveNewsletter_checkbox_id
        self.receiveSpecialoffers_checkbox_id = CreateAnAccountPageLocators.receiveSpecialoffers_checkbox_id
        self.firstNameDelivery_textbox_id = CreateAnAccountPageLocators.firstNameDelivery_textbox_id
        self.lastNameDelivery_textbox_id = CreateAnAccountPageLocators.lastNameDelivery_textbox_id
        self.companyName_textbox_id = CreateAnAccountPageLocators.companyName_textbox_id
        self.address_textbox_id = CreateAnAccountPageLocators.address_textbox_id
        self.addressLine2_textbox_id = CreateAnAccountPageLocators.addressLine2_textbox_id
        self.city_textbox_id = CreateAnAccountPageLocators.city_textbox_id
        self.state_dropdownmenu_id = CreateAnAccountPageLocators.state_dropdownmenu_id
        self.state_menuitem_visibletext = CreateAnAccountPageLocators.state_menuitem_visibletext
        self.postCode_textbox_id = CreateAnAccountPageLocators.postCode_textbox_id
        self.contry_dropdownmenu_id = CreateAnAccountPageLocators.contry_dropdownmenu_id
        self.additionalInformation_textbox_id = CreateAnAccountPageLocators.additionalInformation_textbox_id
        self.mobilePhone_textbox_id = CreateAnAccountPageLocators.mobilePhone_textbox_id
        self.aliasForAddress_textbox_id = CreateAnAccountPageLocators.aliasForAddress_textbox_id
        self.submitAccount_btn_id = CreateAnAccountPageLocators.submitAccount_btn_id

    def click_On_Mr(self):
        self.driver.find_element_by_id(self.genderMr_radiobtn_id).click()

    def click_On_Mrs(self):
        self.driver.find_element_by_id(self.genderMrs_radiobtn_id).click()

    def enter_FName(self, first_name):
        self.driver.find_element_by_id(self.userFirstName_textbox_id).send_keys(first_name)

    def enter_LName(self, second_name):
        self.driver.find_element_by_id(self.userSecondName_textbox_id).send_keys(second_name)

    def enter_Email(self, email):
        self.driver.find_element_by_id(self.userEmail_textbox_id).send_keys(email)

    def enter_Passw(self, passw):
        self.driver.find_element_by_id(self.userPasswd_textbox_id).send_keys(passw)

    def select_DayOfBirth(self):
        self.driver.find_element_by_id(self.dayOfBirth_dropdownmenu_id).click()
        Select(self.driver.find_element_by_id(self.dayOfBirth_dropdownmenu_id)).select_by_visible_text(self.dayOfBirth_menuitem_visibletext)

    def select_MonthOfBirth(self):
        self.driver.find_element_by_id(self.monthOfBirth_dropdownmenu_id).click()
        Select(self.driver.find_element_by_id(self.monthOfBirth_dropdownmenu_id)).select_by_visible_text(self.monthOfBirth_menuitem_visibletext)

    def select_YearOfBirth(self):
        self.driver.find_element_by_id(self.yearOfBirth_dropdownmenu_id).click()
        Select(self.driver.find_element_by_id(self.yearOfBirth_dropdownmenu_id)).select_by_visible_text(self.yearOfBirth_menuitem_visibletext)

    def mark_ReceiveNews(self):
        self.driver.find_element_by_id(self.receiveNewsletter_checkbox_id).click()

    def mark_ReceiveSpecOffer(self):
        self.driver.find_element_by_id(self.receiveSpecialoffers_checkbox_id).click()

    def enter_FNameDelivery(self, name):
        self.driver.find_element_by_id(self.firstNameDelivery_textbox_id).send_keys(name)

    def enter_SNameDelivery(self, second_name):
        self.driver.find_element_by_id(self.lastNameDelivery_textbox_id).send_keys(second_name)

    def enter_CompanyName(self, company_name):
        self.driver.find_element_by_class_name(self.companyName_textbox_id).send_keys(company_name)

    def enter_address(self, address):
        self.driver.find_element_by_id(self.address_textbox_id).send_keys(address)

    def enter_addressLine2(self, address_line2):
        self.driver.find_element_by_id(self.addressLine2_textbox_id).send_keys(address_line2)

    def enter_CityName(self, city_name):
        self.driver.find_element_by_id(self.city_textbox_id).send_keys(city_name)

    def select_State(self):
        self.driver.find_element_by_id(self.state_dropdownmenu_id).click()
        Select(self.driver.find_element_by_id(self.state_dropdownmenu_id)).select_by_visible_text(self.state_menuitem_visibletext)

    def enter_PostCode(self, post_code):
        self.driver.find_element_by_id(self.postCode_textbox_id).send_keys(post_code)

    def select_country(self):
        self.driver.find_element_by_id(self.contry_dropdownmenu_id).click()

    def enter_AdditionalInf(self, additional_info):
        self.driver.find_element_by_id(self.additionalInformation_textbox_id).send_keys(additional_info)

    def enter_MobilePhone(self, mobile):
        self.driver.find_element_by_id(self.mobilePhone_textbox_id).send_keys(mobile)

    def enter_AliasForAddress(self, alias):
        self.driver.find_element_by_id(self.aliasForAddress_textbox_id).send_keys(alias)

    def click_SubmitBtn(self):
        self.driver.find_element_by_id(self.submitAccount_btn_id).click()


