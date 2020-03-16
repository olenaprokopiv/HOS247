# Created by lena at 10/5/2019
Feature: Test for main page

  Scenario: Verify that pricing page is opened
    Given Open hos247
    When Click pricing button
    Then Close CHECK OUR PRICES popup
    Then Verify ELD Pricing Plans page header

  Scenario: Verify ELD dropdown menu
    Given Open hos247
    When Hover over ELD dropdown menu
    When Click tutorial
    Then Verify Tutorials page header

  Scenario: search results page is shown
    Given Open hos247
    When  Click title box GPS learn more button Fleet Tracking
    Then Verify results for GPS Fleet Tracking is shown

