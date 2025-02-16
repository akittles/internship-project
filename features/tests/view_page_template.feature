# Created by Owner at 2/16/2025
Feature: View page template feature
  # Enter feature description here

  #    view page template/ send my cv scenario
  Scenario: User can open Send my CV page
    Given Open main page
    Given User enters username and password
    Then User clicks continue
    Then User clicks on market
    Then Verify market page
    Then User clicks Add Company button
    Then Verify Add Company page
    When User clicks page template button
    Then Verify send my cv button
