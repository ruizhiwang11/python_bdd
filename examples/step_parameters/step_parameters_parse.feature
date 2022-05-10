Feature: Passing parameters to step
  Scenario: method 1 of passing step parameters

    Given I have a new "DVD" in my cart
    Given I have a new "BOOK" in my cart
    Given I have a new "car" in my cart
    When I click on "Next"
    And I click on "FINISH"
    Then I should see "success"