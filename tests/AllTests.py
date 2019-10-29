import unittest
import HtmlTestRunner
from selenium import webdriver

import os, sys, inspect
# fetch path to the directory in which current file is, from root directory or C:\ (or whatever driver number it is)
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extract the path to parent directory
parentdir = os.path.dirname(currentdir)
# insert path to the folder from parent directory from which the python module/ file is to be imported
sys.path.insert(0, parentdir+'/Resources')
sys.path.insert(0, parentdir+'/Resources/PO')

from TestData import TestData
from Locators import Locators
from PO import Pages
from Pages import CamerasPage, CartPage


class Test_GoPro_Base(unittest.TestCase):
    
    # Pre - Condition
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH, options=chrome_options)
        self.driver.maximize_window()
        self.driver.get(TestData.BASE_URL)

    # Post - Condition
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


class Test_GoPro_Cart(Test_GoPro_Base):
    
    def setUp(self):
        super().setUp()
        self.camerasPage = CamerasPage(self.driver)
        self.camerasPage.go_to_cameras_page()
        self.camerasPage.add_to_cart()


    # Steps
    def test_add_two_items_to_cart(self):
        self.camerasPage.add_to_cart()

        self.mini_cart_quantity = self.camerasPage.get_text(Locators.MINI_CART_QUANTITY_TEXT)
        self.assertIn("4", self.mini_cart_quantity)

    def test_remove_from_cart(self):
        self.camerasPage.add_to_cart()

        self.cartPage = CartPage(self.driver)
        self.cartPage.go_to_cart_page()
        self.cartPage.remove_item()
        self.cart_quantity = self.cartPage.get_attribute(Locators.QUANTITY_TEXT_BOX, 'value')
        self.assertIn("1", self.cart_quantity)

    def test_delete_from_cart(self):
        self.cartPage = CartPage(self.driver)
        self.cartPage.go_to_cart_page()
        self.cartPage.delete_item()
        self.empty_cart_text = self.cartPage.get_text(Locators.CART_EMPTY_TEXT)
        self.assertIn(TestData.EMPTY_CART_TEXT, self.empty_cart_text)

    def test_remove_from_cart_fail(self):
        self.cartPage = CartPage(self.driver)
        self.cartPage.go_to_cart_page()
        self.cartPage.delete_item()
        self.cartPage.remove_item()
        self.cart_quantity = self.cartPage.get_attribute(Locators.QUANTITY_TEXT_BOX, 'value')
        self.assertIn("1", self.cart_quantity)


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Results'))