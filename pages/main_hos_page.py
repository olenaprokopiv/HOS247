from selenium.webdriver.common.by import By
from hos247.pages.base_page import Page
from time import sleep

class MainPage(Page):

    BUTTON_PRICING_LOCATOR = (By.XPATH, "//ul[@id='menu-new-hos-menu']//a[text()='Pricing']")
    ELD_LOCATOR = (By.XPATH, "//ul[@id='menu-new-hos-menu']//a[@class='dropdown-toggle']" )
    TUTORIALS_LOCATOR = (By.XPATH, "//ul[@class='dropdown-menu']//li//a[text()='Tutorials']")
    BUTTON_LEARN_MORE_LOCATOR = (By.XPATH, "//div[@class='elementor-widget-wrap' and .//a[text()='GPS Fleet Tracking']]//a[@role='button' and .//span[text()='Learn More']]")
    FLEET_TRACKING_LOCATOR = (By.XPATH, "//div[@class='elementor-icon-box-content']//h1//span")

    def open(self):
        self.open_page('https://hos247.com/')

    def click_pricing(self):
        self.click_elem_idx(*self.BUTTON_PRICING_LOCATOR, idx = 1)

    def hover_over_menu(self, *locator):
        self.hover_over_element_idx(*self.ELD_LOCATOR, idx = 1)
        sleep(2)

    def click_tutorial(self):
        self.click_elem_idx(*self.TUTORIALS_LOCATOR, idx = 1)

    def verify_page_header(self, expected_text: str):
        sleep(4)
        self.verify_element_text(expected_text, *self.TUTORIALS_LOCATOR)

    def click_learn_more_button(self):
        sleep(4)
        self.click(*self.BUTTON_LEARN_MORE_LOCATOR)


    def verify_page_header_text(self, expected_text: str):
        sleep(4)
        self.verify_element_text(expected_text, *self.FLEET_TRACKING_LOCATOR)
