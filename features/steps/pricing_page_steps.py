from behave import given, when, then
from time import sleep

@given('Open hos247 pricing page')
def open_hos247_pricing_page(context):
    context.app.pricing_page.open()

@then('Close CHECK OUR PRICES popup')
def close_prices_popup(context):
    context.app.pricing_page.close_prices_popup()
    sleep(4)

@then('Verify {header} page header')
def verify_page_header(context, header):
    context.app.pricing_page.verify_page_header(header)
    sleep(1)

@when('Input name {search_text}')
def input_name(context, search_text):
    print('search_text = ', search_text)
    context.app.pricing_page.input_name(search_text)

@when('Input company name {search_text}')
def input_company_name(context, search_text):
    print('search_text = ', search_text)
    context.app.pricing_page.input_company_name(search_text)

@when('Input email {search_text}')
def input_email(context, search_text):
    print('search_text = ', search_text)
    context.app.pricing_page.input_email(search_text)

@when('Input phone number {search_text}')
def input_phone_number(context, search_text):
    print('search_text = ', search_text)
    context.app.pricing_page.input_phone_number(search_text)

@when('Input fleet size {search_text}')
def input_fleet_size(context, search_text):
    print('search_text = ', search_text)
    context.app.pricing_page.input_fleet_size(search_text)

@then('Click request demo button')
def click_request_demo_button(context):
    context.app.pricing_page.click_request_demo_button()

@then('Verify {header} demo header')
def verify_demo_header(context, header):
    context.app.pricing_page.verify_demo_header(header)
    sleep(1)

@when('Click ELD Compliance Order Now')
def click_order_now(context):
    context.app.pricing_page.click_order_now()