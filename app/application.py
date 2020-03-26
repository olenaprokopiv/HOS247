from pages.main_hos_page import MainPage
from pages.pricing_page import PricingPage
from pages.cart_hos_page import CarthosPage

class Application:
    def __init__(self, driver):
        self.driver = driver

        self.main_hos_page = MainPage(self.driver)
        self.pricing_page = PricingPage(self.driver)
        self.cart_hos_page = CarthosPage(self.driver)