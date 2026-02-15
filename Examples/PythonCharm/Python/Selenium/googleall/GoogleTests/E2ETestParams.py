import unittest

import pytest

from PythonCharm.Python.Selenium.googleall.GogglePages.GoogleMain import GoogleMain
from PythonCharm.Python.Selenium.googleall.GoogleTests.BaseSelenium import BaseSelenium


def setUp(self):
    print('Test Start')


def tearDown(self):
    print('teat down')





@pytest.mark.parametrize(
   'pattern',
     [
            ('dog'),
            ('horse'),
        ]
    )

def test_google_multiple(pattern):
    print ('into test1',pattern)
    base=BaseSelenium()
    driver= base.selenium_init("https://www.google.com")
    main = GoogleMain(driver)
    main.searchForPattern(pattern)
    driver.close()







