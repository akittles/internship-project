# Created by Owner at 12/25/2024
Feature: General info of cards tab(s)
  # Enter feature description here

  Scenario: Tab(s) present on the general info page
    Given Open main page
    Given User enters username and password
    Then User clicks continue
    Then User clicks off plan button
    Then Verify off plan page
    When User clicks on first project
    Then Verify at least one option tab is available
