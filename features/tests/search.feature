
Feature: Tests for search functionality


  Scenario: User can search for a tea on Target
    Given Open target main page
    When Search for tea
    Then Verify search results are shown for tea

Scenario: User can search for a iphone on Target
    Given Open target main page
    When Search for iphone
    Then Verify search results are shown for iphone

  Scenario: User can search for a mug on Target
    Given Open target main page
    When Search for mug
    Then Verify search results are shown for mug

  
    
  Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for coffee
    Then Verify that every product has a name and an image
    


  Scenario: User can see favorite tooltip for search results
    Given Open target main page
    When Search for tea
    And Hover favorite icon
    Then Favorites tooltip is shown