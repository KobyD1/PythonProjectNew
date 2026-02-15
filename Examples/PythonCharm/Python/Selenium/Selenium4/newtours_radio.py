from time import sleep

from selenium.webdriver.common.by import By



class newtours_link(BaseSelenium):


    base = BaseSelenium()
    driver = base.selenium_init("https://demo.guru99.com/selenium/newtours/reservation.php")


    ruond_trip=driver.find_element(By.NAME,"tripType")
    ruond_trip.is_selected()
    ruond_trip.click()


    base.test_end()

    print('test success ')
