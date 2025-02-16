# Created by Owner at 2/1/2025
Feature: Verification page
  # Enter feature description here

  Scenario: User can click on verifications settings option and verify the right page opens
    Given Open main page
    Given User enters username and password
    Then User clicks continue
    When Click on settings
    When User clicks on verification button
    Then Verify verification page
    Then Verify upload image button
    Then Verify next step button

