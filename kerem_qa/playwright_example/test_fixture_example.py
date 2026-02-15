from kerem_qa.playwright_example.pages.login_page import loginPage
import time


class TestLogin():


    def test_calculator(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.calculator.net")
        print ("Test end")

    def test_calculator_with_fixture_2(self,setup_playwright_with_users):
        page = setup_playwright_with_users
        page.goto("https://www.calculator.net")
        print ("Test end")

    def test_login_swag_lab(self,setup_playwright_swaglabs):
        page ,login_page, product_page,excel_utils = setup_playwright_swaglabs
        login_page.login("standard_user","secret_sauce")
        login_page.verify_login_success()

    def test_login_swag_lab_with_incorrect_parameters(self,setup_playwright_swaglabs):
        page,login_page, product_page,excel_utils = setup_playwright_swaglabs
        login_page.login("standard_user","fake")
        login_page.verify_login_fail()


    def test_get_products_prices_to_excel(self,setup_playwright_swaglabs):
        page ,login_page, product_page,excel_utils = setup_playwright_swaglabs
        login_page.login("standard_user","secret_sauce")
        prices = product_page.verify_and_get_product_prices()
        current_seconds = int(time.time())

        path = F"C:/Users/dkdk1/PycharmProjects/pythonProjrctNew/kerem_qa/excel/prices_{current_seconds}.csv"
        excel_utils.set_excel_data(self,prices, path)
        excel_data = excel_utils.get_excel_row_data(self,1, path)
        excel_data.remove('Price')
        assert prices == excel_data, "data did not read from  excel as wrote"











