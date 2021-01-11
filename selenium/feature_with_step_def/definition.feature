Feature:
  @test
  Scenario:
    Given I have a new car in my cart
    When I click on Next button
    And I click on Next button
    And I click on Finish button
    Then It gives me error