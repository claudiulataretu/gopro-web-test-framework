from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, driver):
        self.driver = driver
    
    def click(self, by_locator):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(by_locator)).click()
    
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_text(self, by_locator):
        text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text
        return text
    
    def get_attribute(self, by_locator, attribute):
        _attribute = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).get_attribute(attribute)
        return _attribute