# Created by lena at 4/8/2020
Feature: Test for AI Dispatch page

  Scenario: User can fill out the form
    Given Open hos247 ai-dispatch page
    When Input ai name ppp
    And Input ai company name rrr
    And Input ai email ppprrr@gmail.com
    And Select role Trucker
    And Click Keep me posted
    Then Verify Your message has been submitted. Thank you! in ai page