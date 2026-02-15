import unittest
import pytest
from Examples.ImageAnalyze.common.BaseSelenium import BaseSelenium
from Examples.ImageAnalyze.Utils.ImagesUtils import ImagesUtils
from Examples.ImageAnalyze.ImageGoogleTests.globals import URL


# https://www.iloveimg.com/crop-image  - cropping site

@pytest.mark.flaky(reruns=1)
class ImageExample(unittest.TestCase, BaseSelenium):

    def setUp(self):
        print('Test Start')
        base = BaseSelenium()
        driver = base.selenium_init(URL)
        images_utils = ImagesUtils(driver, False)
        self.images_utils = images_utils
        self.base = base

    def test_image_compare_coardinations_failed(self):
        path_ref_image = "../Images/Ref/Google/logo2_error.png"

        # coardination parameters :x, y (left /down point)
        coardination = {
            'x': 625,
            'y': 50
        }
        is_equals = self.images_utils.compare_image_coardinations(path_ref_image, coardination, 'by coardination_Error')
        self.base.selenium_end()
        assert is_equals == True, 'mismatch found at compare images'

    def test_image_compare_coardinations(self):
        path_ref_image = "../Images/Ref/Google/logo2.png"

        coardination = {
            'x': 625,
            'y': 50
        }
        is_equals = self.images_utils.compare_image_coardinations(path_ref_image, coardination, 'by coardination_pass')
        self.base.selenium_end()
        assert is_equals == True, 'mismatch found at compare images'

    def test_image_compare_error(self):
        path_ref_image = "../Images/Ref/Google/error_1.png"

        coardination = {
            'x': 625,
            'y': 50
        }
        is_equals = self.images_utils.compare_image_coardinations(path_ref_image, coardination, 'error_random_image')
        self.base.selenium_end()
        assert is_equals == True, 'mismatch found at compare images'
    def test_image_compare_change_position(self):
        path_ref_image = "../Images/Ref/Google/logo2.png"

        coardination = {
            'x': 622,
            'y': 51
        }
        is_equals = self.images_utils.compare_image_coardinations(path_ref_image, coardination, 'change_position')
        self.base.selenium_end()
        assert is_equals == True, 'mismatch found at compare images'

    def test_image_compare_list(self):
        images = [(630, 25, "../Images/Ref/Google/logo2.png"),(625, 50, "../Images/Ref/Google/logo2.png"), (625, 50, "../Images/Ref/Google/logo2_error.png")]
        is_equals = self.images_utils.compare_image_list(images, 'list')
        self.base.selenium_end()
        assert is_equals == True, 'mismatch found at compare images'
    def test_image_compare_list_error(self):
        images = [(630, 25, "../Images/Ref/Google/logo2_error.png"),(629, 624, "../Images/Ref/Google/logo2_error.png"), (630, 34, "../Images/Ref/Google/logo2_error.png")]
        is_equals = self.images_utils.compare_image_list(images, 'list_image')
        self.base.selenium_end()
        assert is_equals == True, 'mismatch found at compare images'