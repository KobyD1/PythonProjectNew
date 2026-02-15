import unittest

import pytest

from Examples.PythonCharm.Python.Selenium.googleall.GogglePages.GoogleMain import GoogleMain
from Examples.PythonCharm.Python.Selenium.googleall.GoogleTests.BaseSelenium import BaseSelenium


def setUp(self):
    print('Test Start')


def tearDown(self):
    print('teat down')

@pytest.fixture
def fixture_before():
    # return [Fruit("apple"), Fruit("banana")]
    print ('\n into pixture')
    base=BaseSelenium()
    driver = base.selenium_init("https://www.google.com")
    return driver



def test_google_cat(fixture_before):
    print ("\n into test2")
    driver= fixture_before
    main = GoogleMain(driver)
    main.searchForPattern("cat")
    driver.close()

def test_google_pixture_no_params_examp1(fixture_before):
    print ("\n into test3")
    driver= fixture_before
    main = GoogleMain(driver)
    main.searchForPattern('pattern')
    driver.close()


def test_google_pixture_no_params_examp2(fixture_before):
    print ("\n into test2")
    driver= fixture_before
    main = GoogleMain(driver)
    main.search_for_pattern_updated('cat')
    driver.close()



