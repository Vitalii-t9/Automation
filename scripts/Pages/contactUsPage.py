from scripts.Locators.contactUsPage import ContactUsPageLocators
from scripts.functions import Click

class ContactUs(Click):

    def __init__(self, driver):

        self.driver = driver

        self.contactUs_link_textlink = ContactUsPageLocators.contactUs_link_textlink
        self.subjectHeading_dropdownmenu_id = ContactUsPageLocators.subjectHeading_dropdownmenu_id
        self.subjectHeading_dropdownmenuitem_visibletext = ContactUsPageLocators.subjectHeading_dropdownmenuitem_visibletext
        self.email_textbox_id = ContactUsPageLocators.email_textbox_id
        self.orderReference_dropdownmenu_name = ContactUsPageLocators.orderReference_dropdownmenu_name
        self.orderReference_dropdownmenuitem_visibletext = ContactUsPageLocators.orderReference_dropdownmenuitem_visibletext
        self.product_dropdownmenu_id = ContactUsPageLocators.product_dropdownmenu_id
        self.product_dropdownmenuitem_visibletext = ContactUsPageLocators.product_dropdownmenuitem_visibletext
        self.attachFile_uploader_xpath = ContactUsPageLocators.attachFile_uploader_xpath
        self.message_textbox_id = ContactUsPageLocators.message_textbox_id
        self.send_btn_xpath = ContactUsPageLocators.send_btn_xpath
        self.orderReference_textbox_id = ContactUsPageLocators.orderReference_textbox_id

    def select_item_from_dropdownmenu(self):
        pass
