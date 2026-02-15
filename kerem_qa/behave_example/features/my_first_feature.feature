Feature: Calculator - Add

  Background:
    Given init calculator

  @failureFound
  Scenario: Adding action for positive numbers
    When set first number
    When set second number
    Then get the numbers summery results

    @Sanity
    Scenario: Adding action for negative numbers
      When set first number
      When set third number
      Then get the numbers summery results
