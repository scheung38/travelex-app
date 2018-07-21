 Created by mincheung at 20/07/2018
Feature: County Selected
  # Enter feature description here

  Scenario: Provide join list of countries
    Given a new user selects source country
    When on given url endpoint
    Then the result should be a positive list