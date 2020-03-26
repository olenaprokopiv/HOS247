from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep

class ProducthosPage(Page):
    SELECT_BILLING_LOCATOR = (By.XPATH, "//span[@class='bold_option_element']//select")
    CHOOSE_PACKAGE_LOCATOR = (By.XPATH, "//select[@name='properties[Select Billing]']//option[@value='$17 Monthly']")
    ADD_TO_CART_LOCATOR = (By.XPATH, "//button[@class='ajax-submit action_button add_to_cart bold_clone']")

    def click_select_hos_size(self):
        self.wait_for_element_click(*self.SELECT_BILLING_LOCATOR)
        self.wait_for_element_click(*self.CHOOSE_PACKAGE_LOCATOR)

    def click_add_cart(self):
        self.wait_for_element_click(*self.ADD_TO_CART_LOCATOR)