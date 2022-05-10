Feature: Verifying the home page url goes to the right place

  Scenario: The python home page should have correct title

    Given I go to the site "https://www.python.org/"
    Then the page title should be "Welcome to Python.org"

  Scenario: The Python home page should have correct url

    Given I go to the site "https://www.python.org/"
    Then current url should be "https://www.python.org/"