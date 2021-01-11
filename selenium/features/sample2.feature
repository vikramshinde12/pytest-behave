Feature: Login Page
  Scenario: user logs in
    Given I go to login page
    When I click on login
    Then I should see error


  Scenario: user logs out
    Given I go to login page
    When I click on logout
    Then I should see error