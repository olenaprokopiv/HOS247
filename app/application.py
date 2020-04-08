from pages.main_hos_page import MainPage
from pages.pricing_page import PricingPage
from pages.cart_hos_page import CarthosPage
from pages.product_hos_page import ProducthosPage
from pages.ai_dispatch_hos_page import AidispatchPage

class Application:
    def __init__(self, driver):
        self.driver = driver

        self.main_hos_page = MainPage(self.driver)
        self.pricing_page = PricingPage(self.driver)
        self.cart_hos_page = CarthosPage(self.driver)
        self.product_hos_page = ProducthosPage(self.driver)
        self.ai_dispatch_hos_page = AidispatchPage(self.driver)