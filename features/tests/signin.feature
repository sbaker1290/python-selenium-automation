
Feature: Tests for Sign in functionality

  Scenario: Verify Sign In form opened
    Given Open target main page
    When Click on account icon
    When Click on sign in button
    Then Verify sign in page is opened



  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open sign in page
    And Store original window
    When Click on Target terms and conditions link
    And Switch to new window
    Then Verify Terms and Conditions page is opened
    And Close current page
    And Return to original window
