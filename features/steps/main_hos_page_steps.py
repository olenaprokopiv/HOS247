from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By


@given('Open hos247')
def open_hos247(context):
    context.app.main_hos_page.open()

@when('Click pricing button')
def click_pricing_button(context):
    context.app.main_hos_page.click_pricing()

@when('Hover over ELD dropdown menu')
def hover_over_menu(context):
    context.app.main_hos_page.hover_over_menu()

@when('Click tutorial')
def click_tutorial(context):
    context.app.main_hos_page.click_tutorial()


@when('Click title box GPS learn more button {title}')
def click_learn_more_button(context, title):
    context.app.main_hos_page.click_learn_more_button()

@then('Verify results for {header} is shown')
def verify_page_header_text(context, header):
    context.app.main_hos_page.verify_page_header_text(header)
    sleep(1)




