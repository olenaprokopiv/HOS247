from behave import given, when, then
from time import sleep

@given('Open hos247 cart page')
def open_hos247(context):
    context.app.cart_hos_page.open()

@when('Click cart button')
def click_cart_hos_button(context):
    context.app.cart_hos_page.click_cart_hos_button()

@then('Verify {text} in the title')
def verify_title_header_text(context, text):
    context.app.cart_hos_page.verify_hos_page_header_text(text)