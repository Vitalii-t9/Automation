import time

from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

class Action:

    def __init__(self):
        self.locatorTypes = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]


    def click_on_locator(self,logger, locator):
        dictionary = self.__dict__
        try:
            for locatorType in self.locatorTypes:
                if self.find_name(dictionary, locator)[-1] == locatorType.replace(" ", ""):
                    self.driver.find_element(locatorType, locator).click()
                    logger.info(f"locator type '{locatorType}' locator '{locator}' was found")
                    return True
        except NoSuchElementException:
            logger.error(f"locator '{locator}' was not found on the page!!!")
            return False 
        
        # if self.find_name(dictionary, locator)[-1] == "id":
        #     self.driver.find_element_by_id(locator).click()
        # elif self.find_name(dictionary, locator)[-1] == "class":
        #     self.driver.find_element_by_class_name(locator).click()
        # elif self.find_name(dictionary, locator)[-1] == "xpath":
        #     self.driver.find_element_by_xpath(locator).click()
        # elif self.find_name(dictionary, locator)[-1] == "textlink":
        #     self.driver.find_element_by_link_text(locator).click()
        # elif self.find_name(dictionary, locator)[-1] == "cssselectors":
        #     self.driver.find_element_by_css_selector(locator).click()
        # elif self.find_name(dictionary, locator)[-1] == "name":
        #     self.driver.find_element_by_name(locator).click()
        # else:
        #     print("Issue!!!")
        
    def select_by_visibletext(self, logger, locator, visible_text):
        dictionary = self.__dict__
        try:
            if self.find_name(dictionary, locator)[-2] == "dropdownmenu":
                for locatorType in self.locatorTypes:
                    if self.find_name(dictionary, locator)[-1] == locatorType.replace(" ", ""):
                        self.driver.find_element(locatorType, locator).click()
                        Select(self.driver.find_element(locatorType, locator)).select_by_visible_text(visible_text)
                        logger.info(f"locator type '{locatorType}' locator '{locator}' was found and selected by visible text successful")
                        return True
        except NoSuchElementException:
            logger.error(f"locator '{locator}' was not found on the page!!!")
            return False 
            
            # if self.find_name(dictionary, locator)[-1] == "id":
            #     self.driver.find_element_by_id(locator).click()
            #     Select(self.driver.find_element_by_id(locator)).select_by_visible_text(visible_text)
            # elif self.find_name(dictionary, locator)[-1] == "class":
            #     self.driver.find_element_by_class_name(locator).click()
            #     Select(self.driver.find_element_by_class_name(locator)).select_by_visible_text(visible_text)
            # elif self.find_name(dictionary, locator)[-1] == "xpath":
            #     self.driver.find_element_by_xpath(locator).click()
            #     Select(self.driver.find_element_by_xpath(locator)).select_by_visible_text(visible_text)
            # elif self.find_name(dictionary, locator)[-1] == "textlink":
            #     self.driver.find_element_by_link_text(locator).click()
            #     Select(self.driver.find_element_by_link_text(locator)).select_by_visible_text(visible_text)
            # elif self.find_name(dictionary, locator)[-1] == "cssselectors":
            #     self.driver.find_element_by_css_selector(locator).click()
            #     Select(self.driver.find_element_by_css_selector(locator)).select_by_visible_text(visible_text)
            # elif self.find_name(dictionary, locator)[-1] == "name":
            #     self.driver.find_element_by_name(locator).click()
            #     Select(self.driver.find_element_by_name(locator)).select_by_visible_text(visible_text)
            # else:
            #     print("Issue!!!")

    def enter_text(self, logger, locator, text):
        dictionary = self.__dict__
        try:
            if self.find_name(dictionary, locator)[-2] == "textbox":
                for locatorType in self.locatorTypes:
                    if self.find_name(dictionary, locator)[-1] == locatorType.replace(" ", ""):
                        self.driver.find_element( locatorType, locator).clear()
                        logger.info(f" text box with locator type '{locatorType}' locator '{locator}' was cleared successful")
                        self.driver.find_element(locatorType, locator).send_keys(text)
                        logger.info(f"enter text in the text box with locator type '{locatorType}' locator '{locator}'")
                        return True
        except NoSuchElementException:
            logger.error(f"locator '{locator}' was not found on the page!!!")
            return False 
        
            
            # if self.find_name(dictionary, locator)[-1] == "id":
            #     self.driver.find_element_by_id(locator).clear()
            #     self.driver.find_element_by_id(locator).send_keys(text)
            # elif self.find_name(dictionary, locator)[-1] == "class":
            #     self.driver.find_element_by_class_name(locator).clear()
            #     self.driver.find_element_by_class_name(locator).send_keys(text)
            # elif self.find_name(dictionary, locator)[-1] == "xpath":
            #     self.driver.find_element_by_xpath(locator).clear()
            #     self.driver.find_element_by_xpath(locator).send_keys(text)
            # elif self.find_name(dictionary, locator)[-1] == "textlink":
            #     self.driver.find_element_by_link_text(locator).clear()
            #     self.driver.find_element_by_link_text(locator).send_keys(text)
            # elif self.find_name(dictionary, locator)[-1] == "cssselectors":
            #     self.driver.find_element_by_css_selector(locator).clear()
            #     self.driver.find_element_by_css_selector(locator).send_keys(text)
            # elif self.find_name(dictionary, locator)[-1] == "name":
            #     self.driver.find_element_by_name(locator).clear()
            #     self.driver.find_element_by_name(locator).send_keys(text)
            # else:
            #     print("Issue!!!")


    def find_name(self, dic, locator):
        for k, v in dic.items():
            if dic[k] == locator:
                return k.split("_")


    def isCorrectEnteredText(self, logger, locator, text):
        pass

    
    # def action(self,  locator, dictionary):
    #     locatorTypes = self.locatorTypes
    #     for locatorType in locatorTypes:
    #         if self.find_name(dictionary, locator)[-1] == locatorType.replace(" ", ""):
    #             self.driver.find_element(locatorType, locator).click()
      
    #     else:
    #         print("Issue!!!")

    # TO DO  add functions to check: 1 is element on page, 2 is text was entered, and all actions was done !!!!