Feature: Error messages during login process

  Scenario Outline: user can not login without entering "<field>"
    Given user is not logged in
    When user types "<value>" in "<field>"
    And user clicks Login button
    Then warning is shown that no match email or password

  Examples:
    | field    | type  | value                      |
    | email    | valid | svetlana.match685@gmail.com  |
    | password | valid | qwerty123                  |