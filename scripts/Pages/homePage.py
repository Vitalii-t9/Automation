from scripts.Locators.homePage import HomePageLocators
from scripts.functions import Click


class HomePage(Click):

    def __init__(self, driver):
        self.driver = driver

        self.signin_link_textlink = HomePageLocators.signIn_link_textlink
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
        self.closeAddToCartPopUp_btn_cssselector = HomePageLocators.closeAddToCartPopUp_btn_cssselector





