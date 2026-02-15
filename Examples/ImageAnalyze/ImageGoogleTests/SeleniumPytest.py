import unittest

from Examples.ImageAnalyze.ImageGogglePages.GoogleMain import GoogleMain
from Examples.ImageAnalyze.common.BaseSelenium import BaseSelenium

class SeleniumPytest(unittest.TestCase,BaseSelenium):

    def setUp(self):
        print ('Test Start')
        self.base=BaseSelenium()
        self.driver= self.base.selenium_init("https://www.google.com")
        self.main=GoogleMain(self.driver)

    def tearDown(self) :
        self.base.selenium_end()




    def test_google_cat(self):
        self.main.searchForPattern("cat")

    def test_google_dog(self):
        main=GoogleMain(self.driver)
        main.searchForPattern("Dog")













