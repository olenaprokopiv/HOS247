# Created by lena at 3/25/2020
Feature: Test for cart page

  Scenario: Shopping cart - empty state
    Given Open hos247 cart page
    When Click cart button
    Then Verify YOUR CART IS EMPTY in the title