from selenium.webdriver.chrome import webdriver


def test_init() :
    driver = webdriver.Chrome(executable_path="../driver/chromedriver102.exe")
    driver.maximize_window()


def test_end(driver):
    driver.quit()
    print('test success ')