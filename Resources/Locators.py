from selenium.webdriver.common.by import By

class Locators():
    #BUTTONS
    CAMERAS_PAGE_BUTTON = (By.CLASS_NAME, "cameras")
    ADD_TO_CART_BUTTON = (By.XPATH, "//*[@title='Click here to add HERO8 Black to cart.']")
    VIEW_CART_BUTTON = (By.CLASS_NAME, "mini-cart-viewcart-cta")
    CLOSE_CART_BUTTON = (By.ID, "minicart-popup-close")
    MINI_CART_BUTTON = (By.CLASS_NAME, "gpn-shopping-cart-display-container")
    PLUS_BUTTON = (By.CLASS_NAME, "button-plus")
    MINUS_BUTTON = (By.CLASS_NAME, "button-minus")
    REMOVE_BUTTON = (By.ID, "deleteProduct")
    
    # TEXT
    MINI_CART_QUANTITY_TEXT = (By.CLASS_NAME, "gpn-cart-count")
    QUANTITY_TEXT_BOX = (By.CLASS_NAME, "quantity-field")
    CART_EMPTY_TEXT = (By.CLASS_NAME, "cart-empty")