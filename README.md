# GoPro Web Testing Framework

This web automation testing framework is designed to automate test cases for the GoPro.com website. It provides basic functionalities to create custom pages with different interactions based on simple commands:
- Click on a button
- Get visibility state for a HTML element
- Get text from a HTML element
- Get attribute value from a HTML element
Further atomic commands can be added to the BasePageClass available under the Resources/PO/BasePageClass.py

Based on the atomic methods new particular actions can be implemented that requires chaining multiple simple commands. The Pages.py provides inherited classes for Cameras Page and Cart Page which provides methods:
    CamerasPage:
        - Add camera to cart

    Cart Page:
        - Increase items quantity in cart
        - Decrease items quantity in cart
        - Delete items from cart

Test cases represents a sequence of actions from which an assert is made. The test cases can be found in tests folder. A base class called Test_GoPro_Base hodls the initialization(setUp method) for all the test cases and the closing environment(tearDown method). These are generic actions needed for all test cases which includes:
- initilize the web driver object. Various web browsers can be used by specifing the web driver through the TestData class. Only Chrome was tested for this implementation
- navigate to the home page of GoPro website
- close the web window
Based on this base testing class The Test_GoPro_Cart class holds the actual test cases.

POM pattern is used to abstract the page elements used for interaction. The Locators.py file from Resources holds references for elements used for test cases actions. Whenever the element identifier is changed, the Locators.py will be the only place from which it should be modified.


# Test automation framework - Requirements
- Linux OS
- Python 3(tested with 3.6)
- Python-pip package
- Install python packages requirements
```
pip install requirements.txt
```

# Test automation framework - Run
- Run all tests
`python tests/AllTests.py`
- Run a single test
`python tests/AllTests.py -v Test_GoPro_Cart.test_add_two_items_to_cart`

Tests report will be available under Results folder