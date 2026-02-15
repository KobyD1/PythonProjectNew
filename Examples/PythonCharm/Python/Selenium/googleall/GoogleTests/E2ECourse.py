import unittest

import pytest

from Examples.PythonCharm.Python.Selenium.googleall.GogglePages.GoogleMain import GoogleMain
from Examples.PythonCharm.Python.Selenium.googleall.GoogleTests.BaseSelenium import BaseSelenium




class googleCat():


        print ("\n into test2")
        base=BaseSelenium()
        driver = base.selenium_init("https://www.google.com")
        main = GoogleMain(driver)
        main.searchForPattern("cat")
        driver.close()




