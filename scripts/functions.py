from selenium.webdriver.support.ui import Select
class Click:

    def click_on_locator(self, locator):
        dictionary = self.__dict__
        if find_name(dictionary, locator)[-1] == "id":
            self.driver.find_element_by_id(locator).click()
        elif find_name(dictionary, locator)[-1] == "class":
            self.driver.find_element_by_class_name(locator).click()
        elif find_name(dictionary, locator)[-1] == "xpath":
            self.driver.find_element_by_xpath(locator).click()
        elif find_name(dictionary, locator)[-1] == "textlink":
            self.driver.find_element_by_link_text(locator).click()
        elif find_name(dictionary, locator)[-1] == "cssselectors":
            self.driver.find_element_by_css_selector(locator).click()
        elif find_name(dictionary, locator)[-1] == "name":
            self.driver.find_element_by_name(locator).click()
        else:
            print("Issue!!!")

    def select_by_visibletext(self, locator, visible_text):
        dictionary = self.__dict__
        if find_name(dictionary, locator)[-2] == "dropdownmenu":
            if find_name(dictionary, locator)[-1] == "id":
                self.driver.find_element_by_id(locator).click()
                Select(self.driver.find_element_by_id(locator)).select_by_visible_text(visible_text)
            elif find_name(dictionary, locator)[-1] == "class":
                self.driver.find_element_by_class_name(locator).click()
                Select(self.driver.find_element_by_class_name(locator)).select_by_visible_text(visible_text)
            elif find_name(dictionary, locator)[-1] == "xpath":
                self.driver.find_element_by_xpath(locator).click()
                Select(self.driver.find_element_by_xpath(locator)).select_by_visible_text(visible_text)
            elif find_name(dictionary, locator)[-1] == "textlink":
                self.driver.find_element_by_link_text(locator).click()
                Select(self.driver.find_element_by_link_text(locator)).select_by_visible_text(visible_text)
            elif find_name(dictionary, locator)[-1] == "cssselectors":
                self.driver.find_element_by_css_selector(locator).click()
                Select(self.driver.find_element_by_css_selector(locator)).select_by_visible_text(visible_text)
            elif find_name(dictionary, locator)[-1] == "name":
                self.driver.find_element_by_name(locator).click()
                Select(self.driver.find_element_by_name(locator)).select_by_visible_text(visible_text)
            else:
                print("Issue!!!")

    def enter_text(self, locator, text):
        dictionary = self.__dict__
        if find_name(dictionary, locator)[-2] == "textbox":
            if find_name(dictionary, locator)[-1] == "id":
                self.driver.find_element_by_id(locator).clear()
                self.driver.find_element_by_id(locator).send_keys(text)
            elif find_name(dictionary, locator)[-1] == "class":
                self.driver.find_element_by_class_name(locator).clear()
                self.driver.find_element_by_class_name(locator).send_keys(text)
            elif find_name(dictionary, locator)[-1] == "xpath":
                self.driver.find_element_by_xpath(locator).clear()
                self.driver.find_element_by_xpath(locator).send_keys(text)
            elif find_name(dictionary, locator)[-1] == "textlink":
                self.driver.find_element_by_link_text(locator).clear()
                self.driver.find_element_by_link_text(locator).send_keys(text)
            elif find_name(dictionary, locator)[-1] == "cssselectors":
                self.driver.find_element_by_css_selector(locator).clear()
                self.driver.find_element_by_css_selector(locator).send_keys(text)
            elif find_name(dictionary, locator)[-1] == "name":
                self.driver.find_element_by_name(locator).clear()
                self.driver.find_element_by_name(locator).send_keys(text)
            else:
                print("Issue!!!")


def find_name(dic, locator):
    for k, v in dic.items():
        if dic[k] == locator:
            return k.split("_")