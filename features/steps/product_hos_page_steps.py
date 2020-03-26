from behave import given, when, then

@when('Select Billing {package}')
def click_select_hos_size(context, package):
    context.app.product_hos_page.click_select_hos_size()

@when('Add {product} to cart')
def click_add_cart(context, product):
    context.app.product_hos_page.click_add_cart()


