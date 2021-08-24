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



