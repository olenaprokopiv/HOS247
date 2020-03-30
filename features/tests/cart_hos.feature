#Created by lena at 3/25/2020
Feature: Test for cart page

#  Scenario: Shopping cart - empty state
#    Given Open hos247 cart page
#    When Click cart button
#    Then Verify YOUR CART IS EMPTY in the title
#
#  Scenario: User is able to add an item to the Shopping Cart
#    Given Open hos247 pricing page
#    Then Close CHECK OUR PRICES popup
#    When Click ELD Compliance Order Now
#    When Select Billing $17 Monthly
#    When Add Billing to cart
#    When Click view cart
#    Then Verify quantity 1

  Scenario: User is able to add an item to the Shopping Cart
    Given Open hos247 pricing page
    Then Close CHECK OUR PRICES popup
    When Click ELD Compliance Order Now
    When Select Billing $17 Monthly
    When Add Billing to cart
    When Click view cart
    When Click remove
    Then Continue shopping

