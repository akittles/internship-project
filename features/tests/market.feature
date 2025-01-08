# Created by Owner at 12/25/2024
Feature: Pagination through market feature
  # Enter feature description here

  Scenario: User can open market tab and go through the pagination
    Given Open main page
    Given User enters username and password
    Then User clicks continue
    Then User clicks on market
    Then Verify market page
    When User pages forward through market
    When User pages backwards through market




#  for next task
#  developer tab "div[fs-queryparam-name=markettagdeveloper"
#  license tag "div.license-block"---for tag in all_tags...