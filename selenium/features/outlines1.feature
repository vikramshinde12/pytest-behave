@dev
Feature: Page color logged in
Scenario Outline: Logged in as <gender> user

    Given I create <gender> user
      """
      This is simple text
      """
    When I login with the user
     """
     {"fist": "bus"}
     """
    Then the page color should <page colour>

    Examples:
      | gender | page colour |
      | female | pink |
      | male | blue |