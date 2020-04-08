from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class AidispatchPage(Page):

    SELECT_ROLE_LOCATOR = (By.XPATH, "//select[@id='field_jq6hf']")
    CHOOSE_TRUCKER_LOCATOR = (By.XPATH, "//select[@id='field_jq6hf']//option[@value='Trucker']")
    NAME_INPUT = (By.XPATH, "//input[@id='field_qy05f87']")
    COMPANY_NAME_INPUT = (By.XPATH, "//input[@id='field_g4mz7']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='field_3asv297']")
    POSTED_LOCATOR = (By.XPATH, "//div[@class='frm_submit']//input[@type='submit']")
    AI_TOOL_BAR_TEXT = (By.XPATH, "//div[@class='frm_message']//p")

    def open(self):
        self.open_page('https://hos247.com/ai-dispatch/')

    def input_ai_name(self, text_name: str):
        print('text email = ', text_name)
        sleep(2)
        self.input(text_name, *self.NAME_INPUT)

    def input_ai_company_name(self, text_company_name: str):
        print('text email = ', text_company_name)
        sleep(2)
        self.input(text_company_name, *self.COMPANY_NAME_INPUT)

    def input_ai_email(self, text_email: str):
        sleep(2)
        print('text email = ', text_email)
        self.input(text_email, *self.EMAIL_INPUT)

    def click_select_ai_role(self):
        self.click(*self.SELECT_ROLE_LOCATOR)
        self.click(*self.CHOOSE_TRUCKER_LOCATOR)

    def click_keep_me_posted(self):
        self.click(*self.POSTED_LOCATOR)

    def verify_header(self, expected_text: str):
        self.verify_element_text(expected_text, *self.AI_TOOL_BAR_TEXT)
