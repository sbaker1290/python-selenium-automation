
Feature: Test for Target cart

  Scenario: Verify “Your cart is empty” message is shown in cart
    Given Open target main page
    When Click on cart icon
    Then Verify empty message is shown