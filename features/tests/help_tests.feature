
Feature: Tests for Help pages

  Scenario: User can select Help topic Promotions & Coupons
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Promotions & Coupons
    Then Verify help Current promotions page opened


  Scenario: User can select Help topic Orders & Purchases
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Orders & Purchases
    Then Verify help Print a receipt page opened
