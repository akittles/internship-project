# Created by Owner at 12/8/2024
Feature: Filter feature
  # Enter feature description here

  Scenario: User can filter unit price (AED)
    Given Open main page
    Given User enters username and password
    Then User clicks continue
    Then User clicks off plan button
    When User clicks filters
    When User enter 1200000 and 2000000 in price filter
    When Click on apply filter
    Then Verify prices on each page is in range
    Then Click on next page
