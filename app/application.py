from hos247.pages.main_hos_page import MainPage
from hos247.pages.pricing_page import PricingPage


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.main_hos_page = MainPage(self.driver)
        self.pricing_page = PricingPage(self.driver)