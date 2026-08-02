import pytest


def test_negative_login_incorrect_user(setup_browser):
    """Negative test: attempting to login with a non-existing user should not show the Login button and should fail.
    The usersPage.select_user method asserts that the Login button is visible after selecting a user,
    so selecting an invalid user is expected to raise an AssertionError.
    """
    page, login_page, users_page, welcome_page, transactions_page = setup_browser

    # go to customer login
    login_page.login()

    # selecting a non-existing user should cause an assertion inside select_user
    with pytest.raises(AssertionError):
        users_page.select_user("This User Does Not Exist")
