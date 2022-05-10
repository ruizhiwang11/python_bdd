Feature: Navigation bars in the home page
  Scenario: Verifying the navigation bars on home page are visible

    Given I go to the site "https://www.python.org"
    Then the "main navigation" bar should be visible
    And the "top navigation" bar should be visible
    And the "options" bar should be visible