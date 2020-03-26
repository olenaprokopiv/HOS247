from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep

class PricingPage(Page):

    ICON_BOX_PRICING = (By.XPATH, "//div[@class='elementor-icon-box-content']//h1//span")
    POPUP_CLOSE_BUTTON = (By.XPATH, "//i[@class='eicon-close']")
    NAME_INPUT = (By.ID, 'field_qy05f86')
    COMPANY_NAME_INPUT = (By.ID, 'field_lvu70')
    EMAIL_INPUT = (By.ID, 'field_3asv296')
    PHONE_NUMER_INPUT = (By.ID, 'field_z7qno')
    FLEET_SIZE_INPUT = (By.ID, 'field_x1z2y')
    BUTTON_REQUEST_DEMO_LOCATOR = (By.XPATH, "//div[@class='frm_submit']//input")
    ICON_BOX_SUBMITT = (By.XPATH, "//div[@class='frm_message']//p[text()='Your message has been submitted. Thank you!']")
    ORDER_NOW_LOCATOR = (By.XPATH, "//div[@class='elementor-repeater-item-ywynofq th-pricing-column col-md-4 col-sm-6' and .//div[text()='ELD Compliance']]//a[text()=' Order Now ']")


    def open(self):
        self.open_page('https://hos247.com/eld-pricing/')

    def close_prices_popup(self):
        self.wait_for_element_click(*self.POPUP_CLOSE_BUTTON)

    def verify_page_header(self, expected_text: str):
        sleep(4)
        self.verify_element_text(expected_text, *self.ICON_BOX_PRICING)

    def input_name(self, text_name: str):
        sleep(4)
        print('text email = ', text_name)
        self.input(text_name, *self.NAME_INPUT)

    def input_company_name(self, text_company_name: str):
        print('text email = ', text_company_name)
        self.input(text_company_name, *self.COMPANY_NAME_INPUT)


    def input_email(self, text_email: str):
        print('text email = ', text_email)
        self.input(text_email, *self.EMAIL_INPUT)

    def input_phone_number(self, text_phone_number: str):
        print('text email = ', text_phone_number)
        self.input(text_phone_number, *self.PHONE_NUMER_INPUT)

    def input_fleet_size(self, text_fleet_size: str):
        print('text email = ', text_fleet_size)
        self.input(text_fleet_size, *self.FLEET_SIZE_INPUT)

    def click_request_demo_button(self):
        sleep(2)
        self.click(*self.BUTTON_REQUEST_DEMO_LOCATOR)

    def verify_demo_header(self, expected_text: str):
        sleep(4)
        self.verify_element_text(expected_text, *self.ICON_BOX_SUBMITT)

    def click_order_now(self):
        self.wait_for_element_appear(*self.ORDER_NOW_LOCATOR)
        self.wait_for_element_click(*self.ORDER_NOW_LOCATOR)