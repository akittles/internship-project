# Created by Owner at 11/7/2024
Feature: Accessing Whatsapp and Telegram
  # Enter feature description here

  Scenario: User can access Whatsapp and Telegram Enter
    Given Open main page
    Given User enters username and password
    Then User clicks continue
    When Click on settings
    When Store original window
    When Click on support
    When Switch to new window
    Then Verify Whatsapp page
##    And Close current page
    And Return to original page
    When Click on news
    Then Verify Telegram page

