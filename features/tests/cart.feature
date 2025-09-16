
Feature: Test for Cart functionality

  Scenario: Verify “Your cart is empty” message is shown in cart
    Given Open target main page
    When Click on cart icon
    Then Verify “Your cart is empty” message is shown



  Scenario: User can add a product to cart
    Given Open target main page
    When Search for candle
    And Click on add to cart button
    And Store product name
    And Confirm Add to cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item(s)
