from t105.selenium_example.selenium_base_105 import seleniumBase105

base = seleniumBase105()
driver = base.selenium_start_with_url("https://demo.guru99.com/test/newtours/index.php")


base.selenium_end()