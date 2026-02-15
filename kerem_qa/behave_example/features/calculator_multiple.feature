Feature: Calculator - Multiple

  Background:
    Given init calculator

  Scenario: Multiple action for 2 positive numbers
    When set first number
    When set second number
    Then get the numbers multiple results

    Scenario: Multiple action for 2 negative number
      When set third number
      When set first number
      Then get the numbers multiple results


