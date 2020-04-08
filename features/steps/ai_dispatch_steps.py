from behave import given, when, then
from time import sleep

@given('Open hos247 ai-dispatch page')
def open_hos247_ai_dispatch(context):
    context.app.ai_dispatch_hos_page.open()

@when('Input ai name {search_text}')
def input_ai_name(context, search_text):
    print('search_text = ', search_text)
    context.app.ai_dispatch_hos_page.input_ai_name(search_text)

@when('Input ai company name {search_text}')
def input_ai_company_name(context, search_text):
    print('search_text = ', search_text)
    context.app.ai_dispatch_hos_page.input_ai_company_name(search_text)

@when('Input ai email {search_text}')
def input_ai_email(context, search_text):
    print('search_text = ', search_text)
    context.app.ai_dispatch_hos_page.input_ai_email(search_text)

@when('Select role Trucker')
def select_role_trucker(context):
    context.app.ai_dispatch_hos_page.click_select_ai_role()

@when('Click Keep me posted')
def click_keep_me_posted(context):
    context.app.ai_dispatch_hos_page.click_keep_me_posted()

@then('Verify {header} in ai page')
def verify_header(context, header):
    context.app.ai_dispatch_hos_page.verify_header(header)