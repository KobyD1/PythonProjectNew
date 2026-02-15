# from datetime import datetime
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
#
#
# def before_all(context):
#
#     options = Options()
#     options.add_argument("--incognito")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     if IS_HEADLESS:options.add_argument("--headless")
#
#     try:
#         if BROWSER ==0:context.driver = webdriver.Chrome(options=options)
#         if BROWSER ==1:context.driver = webdriver.Firefox(options=options)
#
#         # __next > div.jss30.js-focus-visible > div > div > div > div > div > div:nth-child(6) > div > div.css-ug2o6l > a
#
#         context.driver.maximize_window()
#
#         context.login_page = LoginPage(context.driver)
#         context.products_page = ProductsPage(context.driver)
#         context.cart_page = CartPage(context.driver)
#         context.checkout_page = CheckoutPage(context.driver)
#         context.utils = Utils()
#
#     except Exception as e:
#         print(f"ERROR starting Chrome: {e}")
#         context.driver = None
#
#
# def after_all(context):
#     driver = getattr(context, "driver", None)
#     if driver:
#         driver.quit()
#
# def before_scenario(context, scenario):
#     print("*** TEST START ***")
#
#
# def after_scenario(context, scenario):
#     driver = getattr(context, "driver", None)
#
#     if scenario.status == "failed" and driver:
#         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#         filename = f"{PATH_SCREENSHOTS}{scenario.name}_{timestamp}.png"
#         filename = filename.replace(" ", "_")
#
#         driver.save_screenshot(filename)
#         print(f"failure found-screenshot saved in {filename}")
#
#     print("*** TEST END ***")