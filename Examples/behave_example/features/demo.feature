Feature: Login to SauceDemo

  Scenario: Successful login with valid credentials
    Given I am on the SauceDemo login page
    When I login with username "standard_user" and password "secret_sauce"
    Then I should be redirected to the products page

  Scenario: Successful login with invalid  credentials
    Given I am on the SauceDemo login page
    When Login failed
    Then I should be redirected to the products page
