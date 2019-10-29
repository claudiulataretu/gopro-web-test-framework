import os, sys, inspect
# fetch path to the directory in which current file is, from root directory or C:\ (or whatever driver number it is)
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extract the path to parent directory
parentdir = os.path.dirname(currentdir)


class TestData():
    CHROME_EXECUTABLE_PATH = parentdir+'/Drivers/chromedriver.exe'
    BASE_URL = 'https://www.gopro.com/en/gb'
    EMPTY_CART_TEXT = "Your cart is empty."
