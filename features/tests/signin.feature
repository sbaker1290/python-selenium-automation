
Feature: Tests for Sign in functionality

  Scenario: Verify Sign In form opened
    Given Open target main page
    When Click on account icon
    When Click on sign in button
    Then Verify sign in page is opened