from selenium import webdriver
from selenium.webdriver.support import expected_conditions as condition
import time
driver = webdriver.Chrome("C:\\Users\\vitalii.titov\\PycharmProjects\\automationtests\\drivers\\webdrivers_for_win\\chromedriver_ga\\chromedriver.exe")

driver.get("http://automationpractice.com/index.php")


elements = driver.find_elements_by_class_name("product-name")
for elem in elements:
    if "Printed Dress" in elem.text:
        text = elem.text
        print(text)
cond = condition.text_to_be_present_in_element("product-name", "Printed Dress")
print(cond)


# driver.find_element_by_id("search_query_top").send_keys("newer dress")
# time.sleep(2)
# cond = condition.text_to_be_present_in_element("search_query_top", "newer dress")
# cond2 = condition.text_to_be_present_in_element_value("search_query_top", "newer dress")
# print(cond)
# print(cond2)
# text2 = driver.find_element_by_class_name("search_query").text
# print(text2)
# time.sleep(3)
# driver.close()