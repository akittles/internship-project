# Created by Owner at 12/16/2024
Feature: Off Plan page product pic and title verification
  # Enter feature description here

  Scenario: Cards pictures and title verification
    Given Open main page
    Given User enters username and password
    Then User clicks continue
    Then User clicks off plan button
    Then Verify off plan page
    When Verify cards title
    When Verify cards pictures

   Scenario: Cards filtered by out of stock sales status display out of stock
    Given Open main page
    Given User enters username and password
    Then User clicks continue
    Then User clicks off plan button
    Then Verify off plan page
    When User clicks on sales status filter
    When User clicks on out of stock
    Then Verify out of stock tags

#update application file

#sale_status = driver.find_element_by_id('some-id')
#attr_value = elem.get_attribute('some-attribute')
