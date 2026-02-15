import unittest

import allure


class testDEmo1(unittest.TestCase):

    @allure.title("Login test")
    @allure.description("Verify that a user can log in successfully")
    def test_login(self):
        assert True

    def test_demo1(self):
        assert True