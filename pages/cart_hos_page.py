from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class CarthosPage(Page):

   CART_BUTTON_LOCATOR = (By.XPATH, "//li[@class='cart']//a[@href='#cart']")
   CART_IS_EMPTY = (By.XPATH, "//div[@id='mm-1']//li[@class='empty_cart mm-listitem']")

   def open(self):
       self.open_page('https://store.hos247.com/products/eld-compliance')

   def click_cart_hos_button(self):
       self.wait_for_element_click(*self.CART_BUTTON_LOCATOR)

   def verify_hos_page_header_text(self, expected_text: str):
       self.wait_for_element_appear(*self.CART_IS_EMPTY)
       self.verify_element_text(expected_text, *self.CART_IS_EMPTY)
