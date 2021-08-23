from scripts.Locators.homePage import HomePageLocators
from selenium import webdriver

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.signin_link_text_link = HomePageLocators.signIn_link_textlink
        self.contactUs_link_textlink = HomePageLocators.contactUs_link_textlink
        self.search_textbox_id = HomePageLocators.search_textbox_id
        self.submitSerch_Btn_name = HomePageLocators.submitSerch_Btn_name
        self.cart_link_cssselectors = HomePageLocators.cart_link_cssselectors
        self.womanCatg_link_textlink = HomePageLocators.womanCatg_link_textlink
        self.dressesCatg_link_xpath = HomePageLocators.dressesCatg_link_xpath
        self.tshirtsCatg_link_xpath = HomePageLocators.tshirtsCatg_link_xpath
        self.prevBtnHomeSlider_btn_class = HomePageLocators.prevBtnHomeSlider_btn_class
        self.nextBtnHomeSlider_btn_class = HomePageLocators.nextBtnHomeSlider_btn_class
        self.popular_link_class = HomePageLocators.popular_link_class
        self.bestsellers_link_class = HomePageLocators.bestsellers_link_class
        self.prodItem1_link_xpath = HomePageLocators.prodItem1_link_xpath
        self.prodItem2_link_xpath = HomePageLocators.prodItem2_link_xpath
        self.prodItemQuickView_link_class = HomePageLocators.prodItemQuickView_link_class
        self.prodItemCloseQuickView_class = HomePageLocators.prodItemCloseQuickView_class
        self.addToCartQuickView_btn_class = HomePageLocators.addToCartQuickView_btn_class
        self.prodDeteilView_link_textlink = HomePageLocators.prodDeteilView_link_textlink
        self.addToCart_btn_xpath = HomePageLocators.addToCart_btn_xpath
        self.closeAddToCartPopUp_btn_selector = HomePageLocators.closeAddToCartPopUp_btn_selector

    def click_signIn(self):
        self.driver.find_element_by_link_text(self.signin_link_text_link).click()

    def click_contactUs(self):
        self.driver.find_element_by_link_text(self.contactUs_link_textlink).click()

    def search(self, query):
        self.driver.find_element_by_id(self.search_textbox_id).clear()
        self.driver.find_element_by_id(self.search_textbox_id).send_keys(query)
        self.driver.find_element_by_name(self.submitSerchBtn_name).click()

    def click_cart(self):
        self.driver.find_element_by_css_selector(self.cart_link_cssselectors).click()

    def click_womenCategory(self):
        self.driver.find_element_by_link_text(self.womanCatg_link_textlink).click()

    def click_dressesCategory(self):
        self.driver.find_element_by_xpath(self.dressesCatg_link_xpath).click()

    def click_tshirtsCategory(self):
        self.driver.find_element_by_xpath(self.tshirtsCatg_link_xpath).click()

    def click_prevBtnHomeSlider(self):
        self.driver.find_element_by_class_name(self.prevBtnHomeSlider_btn_class).click()

    def click_nextBtnHomeSlider(self):
        self.driver.find_element_by_class_name(self.nextBtnHomeSlider_btn_class).click()

    def click_popular(self):
        self.driver.find_element_by_class_name(self.popular_link_class).click()

    def click_bestsellers(self):
        self.driver.find_element_by_class_name(self.bestsellers_link_class).click()

    def clickOn_randomProd1(self):
        self.driver.find_element_by_xpath(self.prodItem1_link_xpath).click()

    def clickOn_randomProd2(self):
        self.driver.find_element_by_xpath(self.prodItem2_link_xpath).click()

    def click_ProdQuickView(self):
        self.driver.find_element_by_class_name(self.prodItemQuickView_link_class).click()

    def click_closeProdQuickView(self):
        self.driver.find_element_by_class_name(self.prodItemCloseQuickView_class).click()

    def click_AddtoCartQuickView(self):
        self.driver.find_element_by_class_name(self.addToCartQuickView_btn_class).click()

    def click_more(self):
        self.driver.find_element_by_link_text(self.prodDeteilView_link_textlink).click()

    def click_AddToCart(self):
        self.driver.find_element_by_css_selector(self.addToCart_btn_selector).click()

    def click_closeAddedToCartPopUp(self):
        self.driver.find_element_by_css_selector(self.closeAddToCartPopUp_btn_selector).click()



