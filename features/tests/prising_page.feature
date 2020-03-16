# Created by lena at 3/13/2020
Feature: Test for prising page

  Scenario: Verify that Request a free demo is working
    Given Open hos247 pricing page
    Then Close CHECK OUR PRICES popup
    When Input name ppp
    And  Input company name rrr
    And Input email ppprrr@gmail.com
    And Input phone number 2222222222
    And Input fleet size 1
    Then Click request demo button
    And Verify Your message has been submitted. Thank you! page header