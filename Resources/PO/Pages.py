import os, sys, inspect
# fetch path to the directory in which current file is, from root directory or C:\ (or whatever driver number it is)
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extract the path to parent directory
parentdir = os.path.dirname(currentdir)
# insert path to the folder from parent directory from which the python module/ file is to be imported
sys.path.insert(0, parentdir)
sys.path.insert(0, parentdir+'/Resources/PO')

from BasePageClass import BasePage
from TestData import TestData
from Locators import Locators


class CamerasPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def go_to_cameras_page(self):
        self.click(Locators.CAMERAS_PAGE_BUTTON)

    def add_to_cart(self):
        self.click(Locators.ADD_TO_CART_BUTTON)
        self.click(Locators.CLOSE_CART_BUTTON)


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_cart_page(self):
        self.click(Locators.MINI_CART_BUTTON)

    def add_item(self):
        self.click(Locators.PLUS_BUTTON)
    
    def remove_item(self):
        self.click(Locators.MINUS_BUTTON)

    def delete_item(self):
        self.click(Locators.REMOVE_BUTTON)